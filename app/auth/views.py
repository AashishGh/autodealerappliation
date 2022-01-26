from django.conf import settings
from django.contrib.auth import authenticate, login
from django.urls.base import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .forms import LoginForm, SignUpForm, CustomPasswordResetForm, CustomSetPasswordForm, UserEditForm


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = settings.LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "login"
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SignUpFormView(FormView):
    form_class = SignUpForm
    template_name = "account/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "register"
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        context["form"] = form
        context["msg"] = 'User created - please <a href="/login">login</a>.'
        context["success"] = True
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@method_decorator(login_required, name="dispatch")
class UserProfileView(DetailView):
    model = User
    template_name = "account/profile.html"
    pk_url_kwarg = "id"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "Profile"
        return context


@method_decorator(login_required, name="dispatch")
class UserProfileEditView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "account/edit_profile.html"
    pk_url_kwarg = "id"
    success_message = "User successfully updated"

    def get_success_url(self):
        return reverse("profile", args=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "Profile"
        context["child_segment"] = "Edit"
        return context




class AccountPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("password_reset_done")
    from_mail = settings.EMAIL_HOST_USER


class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy("password_reset_complete")


class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"


# class AccountPasswordChangeView(PasswordChangeView):
#     template_name = "/account/password_reset_confirm.html"


# class AccountPasswordChangeDoneView(PasswordChangeDoneView):
#     template_name = "/account/password_reset_confirm.html"


# class VerifyTokenView(TemplateView):
#     template_name = "account/token.html"


# class VerificationEmailView(TemplateView):
#     template_name = "account/verify_email.html"
