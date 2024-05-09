from django.contrib import admin

from reports.models import Report, ReportTemplate


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
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "id",
        "name",
    )

    # list_filter = (,)

    date_hierarchy = "created_at"
