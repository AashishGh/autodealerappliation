from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse

from vehicle.models import Vehicle

from .models import Purchase
from .forms import PurchaseForm, PurchaseImportForm


def get_filtered_queryset(searchkey, searchvalue):
    return {
        "invoice_no": Purchase.objects.filter(invoice_no__contains=searchvalue),
        "vehicle": Purchase.objects.filter(vehicle__contains=searchvalue),
        "purchase_date": Purchase.objects.filter(purchase_date__contains=searchvalue),
        "price": Purchase.objects.filter(price__contains=searchvalue),
        "vendor_name": Purchase.objects.filter(vendor_name__contains=searchvalue),
        "vendor_address": Purchase.objects.filter(vendor_address__contains=searchvalue),
    }.get(searchkey, Purchase.objects.all())

@method_decorator(login_required, name="dispatch")
class PurchaseListView(ListView):
    model = Purchase
    template_name = "purchase/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(PurchaseListView, self).get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["fields"] = Purchase._meta.get_fields(include_parents=False)
        return context

    def get_queryset(self):
        searchkey = self.request.GET.get("searchkey", None)
        searchvalue = self.request.GET.get("searchvalue", None)
        if searchkey != None:
            return get_filtered_queryset(searchkey, searchvalue)
        else:
            return Purchase.objects.all()


@method_decorator(login_required, name="dispatch")
class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "purchase/detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["child_segment"] = "detail"
        return context


@method_decorator(login_required, name="dispatch")
class PurchaseCreateView(SuccessMessageMixin, CreateView):
    model = Purchase
    template_name = "purchase/create.html"
    form_class = PurchaseForm

    def get_success_message(self, cleaned_data):
        return "Purchase successfully created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["child_segment"] = "create"
        return context


@method_decorator(login_required, name="dispatch")
class PurchaseUpdateView(SuccessMessageMixin, UpdateView):
    model = Purchase
    template_name = "purchase/edit.html"
    form_class = PurchaseForm
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Purchase successfully updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["child_segment"] = "edit"
        return context


@method_decorator(login_required, name="dispatch")
class PurchaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Purchase
    template_name = "purchase/delete.html"
    pk_url_kwarg = "id"
    sucess_url = "scheme/import"

    def get_success_message(self, cleaned_data):
        return "Purchase successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["child_segment"] = "delete"
        return context



import pandas as pd
from pprint import pprint

@method_decorator(login_required, name="dispatch")
class PurchaseImportView(SuccessMessageMixin, FormView):
    form_class = PurchaseImportForm
    template_name = "purchase/import.html"
    success_url = "/purchase/import/"
    success_message = "Purchase successfully imported"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "purchase"
        context["child_segment"] = "import"
        return context

    def form_valid(self, form):
        csvfile = form.cleaned_data.get("csvfile", None)
        if csvfile is not None:
            df = pd.read_csv(csvfile)
            df_dict = df.to_dict(orient="index")
            purchase_list = []
            try:
                for i, v in df_dict.items():
                    vehicle = Vehicle.objects.get(id=v["vehicle id"])

                    purchase_list.append(Purchase(
                        invoice_no=v["invoice number"],
                        vehicle=vehicle,
                        purchase_date=v["purchase date"],
                        price=v["price"],
                        vendor_name=v["vendor name"],
                        vendor_address=v["vendor address"],
                    ))
                    
            except KeyError:
                form.add_error(
                    None,
                    """Column name in file doesn't match!
                     Columns: 
                     'invoice number', 'vehicle id', 'purchase date', 'price', 'vendor name', 'vendor address'""",
                )
                return self.render_to_response(self.get_context_data(form=form))
                
            Purchase.objects.bulk_create(purchase_list)
        return super().form_valid(form)
