import imp
from django.db import IntegrityError
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse

from vehicle.models import Vehicle
from scheme.models import Scheme
from customer.models import Customer

from .models import Sale
from .forms import SaleForm, SaleImportForm


def get_filtered_queryset(searchkey, searchvalue):
    return {
        "invoice_no": Sale.objects.filter(invoice_no__contains=searchvalue),
        "challan_no": Sale.objects.filter(challan_no__contains=searchvalue),
        "vehicle": Sale.objects.filter(vehicle__contains=searchvalue),
        "customer": Sale.objects.filter(customer__contains=searchvalue),
        "sale_date": Sale.objects.filter(sale_date__contains=searchvalue),
        "amount": Sale.objects.filter(amount__contains=searchvalue),
        "discount": Sale.objects.filter(discount__contains=searchvalue),
        "payment_mode": Sale.objects.filter(payment_mode__contains=searchvalue),
        "scheme": Sale.objects.filter(scheme__contains=searchvalue),
        "finance_amount": Sale.objects.filter(finance_amount__contains=searchvalue),
        "exchange_amount": Sale.objects.filter(exchange_amount__contains=searchvalue),
    }.get(searchkey, Sale.objects.all())

@method_decorator(login_required, name="dispatch")
class SaleListView(ListView):
    model = Sale
    template_name = "sale/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(SaleListView, self).get_context_data(**kwargs)
        context["segment"] = "sale"
        context["fields"] = Sale._meta.get_fields(include_parents=False)
        return context
    
    def get_queryset(self):
        searchkey = self.request.GET.get("searchkey", None)
        searchvalue = self.request.GET.get("searchvalue", None)
        if searchkey != None:
            return get_filtered_queryset(searchkey, searchvalue)
        else:
            return Customer.objects.all()


@method_decorator(login_required, name="dispatch")
class SaleDetailView(DetailView):
    model = Sale
    template_name = "sale/detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sale"
        context["child_segment"] = "detail"
        return context


@method_decorator(login_required, name="dispatch")
class SaleCreateView(SuccessMessageMixin, CreateView):
    model = Sale
    template_name = "sale/create.html"
    form_class = SaleForm

    def get_success_message(self, cleaned_data):
        return "Sale successfully created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sale"
        context["child_segment"] = "create"
        return context


@method_decorator(login_required, name="dispatch")
class SaleUpdateView(SuccessMessageMixin, UpdateView):
    model = Sale
    template_name = "sale/edit.html"
    form_class = SaleForm
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Sale successfully updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sale"
        context["child_segment"] = "edit"
        return context


@method_decorator(login_required, name="dispatch")
class SaleDeleteView(SuccessMessageMixin, DeleteView):
    model = Sale
    template_name = "sale/delete.html"
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Sale successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "Sale"
        context["child_segment"] = "delete"
        return context

    def get_success_url(self):
        return reverse("sale-index")


import pandas as pd
from pprint import pprint

@method_decorator(login_required, name="dispatch")
class SaleImportView(SuccessMessageMixin, FormView):
    form_class = SaleImportForm  # import this form
    template_name = "sale/import.html"  # change this
    success_url = "/sale/import/"  # change this
    success_message = "Sale successfully imported"  # change this

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sale"
        context["child_segment"] = "import"
        return context

    def form_valid(self, form):
        csvfile = form.cleaned_data.get("csvfile", None)
        if csvfile is not None:
            df = pd.read_csv(csvfile)
            df_dict = df.to_dict(orient="index")
            sale_list = []
            try:
                 for i, v in df_dict.items():
                    vehicle = Vehicle.objects.get(id=v["vehicle id"])
                    scheme = Scheme.objects.get(id=v["scheme id"])
                    customer = Customer.objects.get(id=v["customer id"])
                    sale_list.append(
                        Sale(
                            invoice_no=v["invoice number"],
                            challan_no=v["challan number"],
                            sale_date=v["sale date"],
                            amount=v["amount"],
                            discount=v["discount"],
                            payment_mode=v["payment mode"],
                            finance_amount=v["finance amount"],
                            exchange_amount=v["exchange amount"],
                            customer=customer,
                            scheme=scheme,
                            vehicle=vehicle,
                        )
                    )
                    
            except KeyError:
                form.add_error(
                    None,
                    """Column name in file doesn't match! 
                    Columns: 
                    'invoice number', 'challan number', 'vehicle id', 'customer', 'sale date', 'amount', 'payment mode', 'scheme', 'finance amount', 'exchange amount'""",
                )
                return self.render_to_response(self.get_context_data(form=form))
            # except ValueError: todo
            # except IntegrityError: todo
            # except ValidationError: todo
            # except TypeError: todo
            Sale.objects.bulk_create(sale_list)
        return super().form_valid(form)
