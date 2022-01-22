from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse

from .models import Scheme
from .forms import SchemeForm, SchemeImportForm


@method_decorator(login_required, name="dispatch")
class SchemeListView(ListView):
    model = Scheme
    template_name = "scheme/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["fields"] = Scheme._meta.get_fields()
        return context


@method_decorator(login_required, name="dispatch")
class SchemeDetailView(DetailView):
    model = Scheme
    template_name = "scheme/detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["child_segment"] = "delete"
        return context


@method_decorator(login_required, name="dispatch")
class SchemeCreateView(SuccessMessageMixin, CreateView):
    model = Scheme
    template_name = "scheme/create.html"
    form_class = SchemeForm
    success_message = "Scheme successfully created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["child_segment"] = "create"
        return context


@method_decorator(login_required, name="dispatch")
class SchemeUpdateView(SuccessMessageMixin, UpdateView):
    model = Scheme
    template_name = "scheme/edit.html"
    form_class = SchemeForm
    pk_url_kwarg = "id"
    success_message = "Scheme successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["child_segment"] = "edit"
        return context


@method_decorator(login_required, name="dispatch")
class SchemeDeleteView(SuccessMessageMixin, DeleteView):
    model = Scheme
    template_name = "scheme/delete.html"
    pk_url_kwarg = "id"
    success_message = "Scheme successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["child_segment"] = "delete"
        return context

    def get_success_url(self):
        return reverse("scheme-index")


import pandas as pd
from pprint import pprint


@method_decorator(login_required, name="dispatch")
class SchemeImportView(SuccessMessageMixin, FormView):
    form_class = SchemeImportForm
    template_name = "scheme/import.html"
    success_url = "/scheme/import/"
    success_message = "Scheme successfully imported"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "scheme"
        context["child_segment"] = "import"
        return context

    def form_valid(self, form):
        csvfile = form.cleaned_data.get("csvfile", None)
        if csvfile is not None:
            df = pd.read_csv(csvfile)
            df_dict = df.to_dict(orient="index")
            try:
                scheme_list = [
                    Scheme(scheme_name=v["scheme name"], description=v["description"])
                    for i, v in df_dict.items()
                ]
            except KeyError:
                form.add_error(
                    None,
                    """Column name in file doesn't match! 
                    Columns: 
                    'scheme name', 'description'""",
                )
                return self.render_to_response(self.get_context_data(form=form))

            objs = Scheme.objects.bulk_create(scheme_list)
            pprint(objs)

        return super().form_valid(form)
