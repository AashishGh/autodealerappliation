from django.urls import path
from .views import (
    SchemeListView,
    SchemeCreateView,
    SchemeDetailView,
    SchemeUpdateView,
    SchemeDeleteView,
    SchemeImportView,
)

urlpatterns = [
    path("", SchemeListView.as_view(), name="scheme-index"),
    path("create/", SchemeCreateView.as_view(), name="scheme-create"),
    path("<int:id>/", SchemeDetailView.as_view(), name="scheme-detail"),
    path("<int:id>/edit", SchemeUpdateView.as_view(), name="scheme-edit"),
    path("<int:id>/delete", SchemeDeleteView.as_view(), name="scheme-delete"),
    path("import/", SchemeImportView.as_view(), name="scheme-import"),
]
