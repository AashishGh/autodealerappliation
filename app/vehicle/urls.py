from django.urls import path
from .views import (
    VehicleListView,
    VehicleDetailView,
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleImportView,
)

urlpatterns = [
    path("", VehicleListView.as_view(), name="vehicle-index"),
    path("create/", VehicleCreateView.as_view(), name="vehicle-create"),
    path("<int:id>/", VehicleDetailView.as_view(), name="vehicle-detail"),
    path("<int:id>/edit", VehicleUpdateView.as_view(), name="vehicle-edit"),
    path("<int:id>/delete", VehicleDeleteView.as_view(), name="vehicle-delete"),
    path("import/", VehicleImportView.as_view(), name="vehicle-import"),
]
