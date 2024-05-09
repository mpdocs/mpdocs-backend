from django.contrib.auth.models import User

from reports.models import Report
from reports.serializers import ReportCreateRequestSerializer


def create_report(serializer: ReportCreateRequestSerializer, user: User) -> Report:
    pass
