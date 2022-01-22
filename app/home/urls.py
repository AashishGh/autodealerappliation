from django.urls import path
from .views import DashboardView, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
