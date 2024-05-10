from django.contrib.auth import get_user_model

from reports.models import Report
from reports.serializers import ReportCreateRequestSerializer

User = get_user_model()


def create_report(serializer: ReportCreateRequestSerializer, user: User) -> Report:
    pass
