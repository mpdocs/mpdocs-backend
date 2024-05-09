from django.urls import path

from reports.views import ReportsListView

app_name = "reports"

urlpatterns = [
    path("", ReportsListView.as_view(), name="reports_list"),
]
