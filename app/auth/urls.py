from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import (
    LoginFormView,
    SignUpFormView,
    UserProfileView,
    AccountPasswordResetView,
    AccountPasswordResetDoneView,
    AccountPasswordResetConfirmView,
    AccountPasswordResetCompleteView,
    UserProfileEditView
    # AccountPasswordChangeView,
    # AccountPasswordChangeDoneView
)

urlpatterns = [
    path("login/", LoginFormView.as_view(), name="login"),
    path("register/", SignUpFormView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<id>/", UserProfileView.as_view(), name="profile"),
    path("profile/<id>/edit", UserProfileEditView.as_view(), name="edit-profile"),
    path("password-reset/", AccountPasswordResetView.as_view(), name="password_reset"),
    path("password-reset/sent", AccountPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", AccountPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/completed", AccountPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
