from django.urls import path
from .views import (
    PurchaseDeleteView,
    PurchaseDetailView,
    PurchaseListView,
    PurchaseCreateView,
    PurchaseUpdateView,
    PurchaseImportView,
)

urlpatterns = [
    path("", PurchaseListView.as_view(), name="purchase-index"),
    path("create/", PurchaseCreateView.as_view(), name="purchase-create"),
    path("<int:id>/", PurchaseDetailView.as_view(), name="purchase-detail"),
    path("<int:id>/edit", PurchaseUpdateView.as_view(), name="purchase-edit"),
    path("<int:id>/delete", PurchaseDeleteView.as_view(), name="purchase-delete"),
    path("import/", PurchaseImportView.as_view(), name="purchase-import"),
]
