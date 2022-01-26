from sqlite3 import IntegrityError
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse

from .models import Vehicle
from .forms import VehicleForm, VehicleImportForm


def get_filtered_queryset(searchkey, searchvalue):
    return {
        "vehicle_model": Vehicle.objects.filter(vehicle_model__contains=searchvalue),
        "color": Vehicle.objects.filter(color__contains=searchvalue),
        "chasis_no": Vehicle.objects.filter(chasis_no__contains=searchvalue),
        "engine_no": Vehicle.objects.filter(engine_no__contains=searchvalue),
        "reg_no": Vehicle.objects.filter(reg_no__contains=searchvalue),
        "key_no": Vehicle.objects.filter(key_no__contains=searchvalue),
        "battery_no": Vehicle.objects.filter(battery_no__contains=searchvalue),
        "mfd_year": Vehicle.objects.filter(mfd_year__contains=searchvalue),
    }.get(searchkey, Vehicle.objects.all())


@method_decorator(login_required, name="dispatch")
class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicle/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["fields"] = Vehicle._meta.get_fields()
        return context

    def get_queryset(self):
        searchkey = self.request.GET.get("searchkey", None)
        searchvalue = self.request.GET.get("searchvalue", None)
        if searchkey != None:
            return get_filtered_queryset(searchkey, searchvalue)
        else:
            return Vehicle.objects.all()

        
@method_decorator(login_required, name="dispatch")
class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = "vehicle/detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["child_segment"] = "delete"
        return context


@method_decorator(login_required, name="dispatch")
class VehicleCreateView(SuccessMessageMixin, CreateView):
    model = Vehicle
    template_name = "vehicle/create.html"
    form_class = VehicleForm

    def get_success_message(self, cleaned_data):
        return "Vehicle successfully created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["child_segment"] = "create"
        return context


@method_decorator(login_required, name="dispatch")
class VehicleUpdateView(SuccessMessageMixin, UpdateView):
    model = Vehicle
    template_name = "vehicle/edit.html"
    form_class = VehicleForm
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Vehicle successfully updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["child_segment"] = "edit"
        return context


@method_decorator(login_required, name="dispatch")
class VehicleDeleteView(SuccessMessageMixin, DeleteView):
    model = Vehicle
    template_name = "vehicle/delete.html"
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Vehicle successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["child_segment"] = "delete"
        return context

    def get_success_url(self):
        return reverse("scheme-index")


import pandas as pd
from pprint import pprint

@method_decorator(login_required, name="dispatch")
class VehicleImportView(SuccessMessageMixin, FormView):
    form_class = VehicleImportForm
    template_name = "vehicle/import.html"
    success_url = "/vehicle/import/"
    success_message = "Vehicle successfully imported"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "vehicle"
        context["child_segment"] = "import"
        return context

    def form_valid(self, form):
        csvfile = form.cleaned_data.get("csvfile", None)
        if csvfile is not None:
            df = pd.read_csv(csvfile)
            df_dict = df.to_dict(orient="index")
            try:
                vehicle_list = [
                    Vehicle(
                        vehicle_model=v["vehicle model"],
                        color=v["color"],
                        chasis_no=v["chasis number"],
                        engine_no=v["engine number"],
                        reg_no=v["registration number"],
                        key_no=v["key number"],
                        battery_no=v["battery number"],
                        mfd_year=v["mfd year"],
                    )
                    for i, v in df_dict.items()
                ]
            except KeyError:
                form.add_error(
                    None,
                    """Column name in file doesn't match! 
                    Columns: 
                    'vehicle model', 'color', 'chasis number', 'engine number',
                    'registration number', 'key number', 'battery number', 'mfd year'""",
                )
                return self.render_to_response(self.get_context_data(form=form))
            except IntegrityError as e:
                # todo - required to be more specific
                form.add_error(
                    None,
                    "Duplicate values for unique field exist in the data",
                )
                return self.render_to_response(self.get_context_data(form=form))


            objs = Vehicle.objects.bulk_create(vehicle_list)
            pprint(objs)
        return super().form_valid(form)
