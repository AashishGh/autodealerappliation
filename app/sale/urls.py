from django.urls import path
from .views import (
    SaleListView,
    SaleDetailView,
    SaleCreateView,
    SaleUpdateView,
    SaleDeleteView,
    SaleImportView,
)

urlpatterns = [
    path("", SaleListView.as_view(), name="sale-index"),
    path("create/", SaleCreateView.as_view(), name="sale-create"),
    path("<int:id>/", SaleDetailView.as_view(), name="sale-detail"),
    path("<int:id>/edit/", SaleUpdateView.as_view(), name="sale-edit"),
    path("<int:id>/delete/q", SaleDeleteView.as_view(), name="sale-delete"),
    path("import/", SaleImportView.as_view(), name="sale-import"),
]
