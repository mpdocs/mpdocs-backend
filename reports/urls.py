from django.urls import path

from reports.views import ReportsListView, ReportDetailView

app_name = "reports"

urlpatterns = [
    path("", ReportsListView.as_view(), name="reports_list"),
    path("<int:pk>/", ReportDetailView.as_view(), name="report_detail"),
]
