from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response

from reports.models import Report, ReportTemplate
from reports.serializers import (
    ReportCreateRequestSerializer,
    ReportCreateResponseSerializer,
    ReportListRequestSerializer,
)


class ReportsListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return ReportCreateRequestSerializer
        return ReportListRequestSerializer

    @extend_schema(
        request=ReportCreateRequestSerializer,
        responses={
            status.HTTP_201_CREATED: ReportCreateResponseSerializer,
        },
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ReportCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            template = ReportTemplate.objects.get(
                pk=serializer.validated_data["template_id"]
            )
        except ReportTemplate.DoesNotExist:
            return Response(
                {"detail": "Report template with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        Report.objects.create(
            user=request.user,
            template=template,
            data=serializer.validated_data,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# todo: вьюшка для получения актуального темплейта
# todo: вьюшка для редактирования отчета
