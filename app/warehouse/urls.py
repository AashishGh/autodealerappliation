from django.urls import path
from .views import WarehouseIndexView

urlpatterns = [
    path("", WarehouseIndexView.as_view(), name="warehouse-index"),
]
