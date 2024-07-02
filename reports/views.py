import datetime
import pathlib
import tempfile

from django.shortcuts import get_object_or_404
from docxtpl import DocxTemplate
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response

from core.permissions import IsStaff
from reports.models import Report, ReportTemplate, StatsTemplate
from reports.permissions import IsReportOwnerOrReadOnly
from reports.renderers import DocxFileRenderer
from reports.serializers import (
    ReportListRequestSerializer,
    ReportListSerializer,
    ReportDetailSerializer,
    ReportDataSerializer,
)

DOCX_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)


class ReportsListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return ReportDataSerializer
        return ReportListSerializer

    @extend_schema(
        request=ReportDataSerializer,
        responses={
            status.HTTP_201_CREATED: ReportDetailSerializer,
        },
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ReportDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template = ReportTemplate.objects.get_latest_active()

        report = Report.objects.create(
            user=request.user,
            template=template,
            data=serializer.validated_data,
        )

        return Response(
            ReportDetailSerializer(report).data, status=status.HTTP_201_CREATED
        )

    @extend_schema(
        request=ReportListRequestSerializer,
        responses={
            status.HTTP_200_OK: ReportListSerializer,
        },
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        return super().get(request, *args, **kwargs)


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    permission_classes = [IsReportOwnerOrReadOnly]
    serializer_class = ReportDetailSerializer

    def put(self, request: Request, *args, **kwargs) -> Response:
        serializer = ReportDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pk = kwargs.get("pk")
        report = get_object_or_404(Report, pk=pk)

        report.data = serializer.validated_data
        report.save()
        return Response(
            status=status.HTTP_200_OK, data=ReportDetailSerializer(report).data
        )

    def patch(self, request: Request, *args, **kwargs) -> Response:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReportGenerateView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    permission_classes = [IsReportOwnerOrReadOnly, IsStaff]
    serializer_class = ReportDetailSerializer
    renderer_classes = [DocxFileRenderer]

    @extend_schema(
        responses={("200", DOCX_CONTENT_TYPE): OpenApiTypes.BINARY},
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        # todo: убрать эту кучу логики из вьюшки и распихать по функциям
        pk = kwargs.get("pk")
        report = get_object_or_404(Report, pk=pk)

        doc = DocxTemplate(report.template.template_file.file)

        context = report.data
        context["first_name"] = report.user.first_name
        context["last_name"] = report.user.last_name
        context["patronymic"] = report.user.patronymic
        context["report_start_date"] = report.template.report_start_date.strftime("%Y")
        context["report_end_date"] = report.template.report_end_date.strftime("%Y")

        doc.render(context)
        filename = (
            f"{request.user.id}-{report.template.name}-{datetime.datetime.now()}.docx"
        )
        generated_filepath = pathlib.Path(tempfile.gettempdir()) / filename

        doc.save(generated_filepath)

        with open(generated_filepath, "rb") as f:
            data = f.read()
            return Response(
                data=data,
                status=status.HTTP_200_OK,
                headers={
                    "Content-Disposition": f'attachment; filename="{filename}"',  # noqa: E702
                    "Content-Type": DOCX_CONTENT_TYPE,
                    "Content-Length": len(data),
                },
            )


class StatsGenerateView(generics.RetrieveAPIView):
    permission_classes = [IsStaff]
    renderer_classes = [DocxFileRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        template = ReportTemplate.objects.get_latest_active()
        reports = Report.objects.filter(template=template)

        context = {
            "employees": [],
            "dissertations": [],  # нет в отчете
            "web_of_science_articles": [],
            "scopus_articles": [],
            "monographs": [],
            "contests": [],
            "conferences": [],
            "patents": [],
            "software_products": [],
            "licenses": [],  # нет в отчете
            "exhibitions": [],
            # нет в отчете
            "cooperation_with_countries": [],
            "international_events": [],
            "student_count_total": 0,
            "student_count_total_with_wages": 0,
            "presentation_count_total": 0,
            "international_presentation_count_total": 0,
            "russian_presentation_count_total": 0,
            "regional_presentation_count_total": 0,
            "exhibit_count_total": 0,
            "international_exhibit_count_total": 0,
            "russian_exhibit_count_total": 0,
            "regional_exhibit_count_total": 0,
            "articles_count_total": 0,
            "articles_count_total_published": 0,
            "student_works_count_total_without_coauthors": 0,
            "student_works_count_total": 0,
            "student_works_count_total_open_contest": 0,
            "award_count_total": 0,
            "award_count_total_open_contest": 0,
            "rid_application_count_total": 0,
            "rip_protection_document_count_total": 0,
            "sold_license_count_total": 0,
            "grant_application_project_count_total": 0,
            "grant_application_project_count_total_winner": 0,
            "olympiad_count_total": 0,
            "olympiad_participant_student_count_total": 0
            # /нет в отчете
        }
        for report in reports:
            user = report.user
            data = report.data
            context["employees"].append({
                "name": f"{user.first_name} {user.last_name} {user.patronymic}",
                "position": data.get("position", ""),
                "academic_degree": data.get("academic_degree", ""),
                "article_count": len(data.get("web_of_science_articles", [])) + len(data.get("scopus_articles", []))
            })
            for category, items in data.items():
                if category in context:
                    context[category].extend(items)

        stats_template = StatsTemplate.objects.order_by("-updated_at").first()
        doc = DocxTemplate(stats_template.template_file.file)

        doc.render(context)
        filename = (
            f"{stats_template.name}-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx"
        )
        generated_filepath = pathlib.Path(tempfile.gettempdir()) / filename

        doc.save(generated_filepath)

        with open(generated_filepath, "rb") as f:
            data = f.read()
            return Response(
                data=data,
                status=status.HTTP_200_OK,
                headers={
                    "Content-Disposition": f'attachment; filename="{filename}"',  # noqa: E702
                    "Content-Type": DOCX_CONTENT_TYPE,
                    "Content-Length": len(data),
                },
            )
