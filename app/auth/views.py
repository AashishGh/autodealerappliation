from re import template
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, SignUpForm


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


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request, "account/register.html", {"form": form, "msg": msg, "success": success}
    )
