import typing

from django.db.models import Manager

if typing.TYPE_CHECKING:
    from reports.models import ReportTemplate


class ReportTemplateManager(Manager):
    def get_latest_active(self) -> "ReportTemplate":
        return (
            self.get_queryset().filter(is_active=True).order_by("-created_at").first()
        )
