from django.urls import path
from .views import (
    CustomerCreateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomerListView,
    CustomerUpdateView,
    CustomerImportView
)

urlpatterns = [
    path("", CustomerListView.as_view(), name="customer-index"),
    path("create/", CustomerCreateView.as_view(), name="customer-create"),
    path("<int:id>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("<int:id>/edit", CustomerUpdateView.as_view(), name="customer-edit"),
    path("<int:id>/delete", CustomerDeleteView.as_view(), name="customer-delete"),
    path("import/", CustomerImportView.as_view(), name="customer-import"),
]
