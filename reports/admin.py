from django.contrib import admin

from reports.models import Report, ReportTemplate, StatsTemplate, Stats


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "is_reviewed",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "created_at",
        "updated_at",
    )

    search_fields = ("id",)

    # list_filter = (,)

    date_hierarchy = "updated_at"


@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "report_start_date",
        "report_end_date",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "name",
        "report_start_date",
        "report_end_date",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "id",
        "name",
    )

    # list_filter = (,)

    date_hierarchy = "created_at"


@admin.register(StatsTemplate)
class StatsTemplateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "template_file",
        "created_at",
        "updated_at",
    )


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "template",
        "report_template",
        "data",
    )

