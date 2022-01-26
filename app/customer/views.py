from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls.base import reverse

from .models import Customer
from .forms import CustomerForm, CustomerImportForm


def get_filtered_queryset(searchkey, searchvalue):
    return {
        "citizenship_no": Customer.objects.filter(citizenship_no__contains=searchvalue),
        "pan_no": Customer.objects.filter(pan_no__contains=searchvalue),
        "fullname": Customer.objects.filter(fullname__contains=searchvalue),
        "dob": Customer.objects.filter(dob__contains=searchvalue),
        "gender": Customer.objects.filter(gender__contains=searchvalue),
        "email": Customer.objects.filter(email__contains=searchvalue),
        "phone": Customer.objects.filter(phone__contains=searchvalue),
        "occupation": Customer.objects.filter(occupation__contains=searchvalue),
        "city": Customer.objects.filter(city__contains=searchvalue),
        "district": Customer.objects.filter(district__contains=searchvalue),
        "state": Customer.objects.filter(state__contains=searchvalue),
        "country": Customer.objects.filter(country__contains=searchvalue),
        "state": Customer.objects.filter(state__contains=searchvalue),
    }.get(searchkey, Customer.objects.all())


@method_decorator(login_required, name="dispatch")
class CustomerListView(ListView):
    model = Customer
    template_name = "customer/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context["segment"] = "customer"
        context["fields"] = Customer._meta.get_fields(include_parents=False)
        return context

    def get_queryset(self):
        searchkey = self.request.GET.get("searchkey", None)
        searchvalue = self.request.GET.get("searchvalue", None)
        if searchkey != None:
            return get_filtered_queryset(searchkey, searchvalue)
        else:
            return Customer.objects.all()


@method_decorator(login_required, name="dispatch")
class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer/detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "customer"
        context["child_segment"] = "detail"
        return context


@method_decorator(login_required, name="dispatch")
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    template_name = "customer/create.html"
    form_class = CustomerForm

    def get_success_message(self, cleaned_data):
        return "Customer successfully created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "customer"
        context["child_segment"] = "create"
        return context


@method_decorator(login_required, name="dispatch")
class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = "customer/edit.html"
    form_class = CustomerForm
    pk_url_kwarg = "id"

    def get_success_message(self, cleaned_data):
        return "Customer successfully updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "customer"
        context["child_segment"] = "edit"
        return context


@method_decorator(login_required, name="dispatch")
class CustomerDeleteView(SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = "customer/delete.html"
    pk_url_kwarg = "id"
    success_url = "customer:customer-index"

    def get_success_message(self, cleaned_data):
        return "Customer successfully deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "customer"
        context["child_segment"] = "delete"
        return context


import pandas as pd
from pprint import pprint


@method_decorator(login_required, name="dispatch")
class CustomerImportView(SuccessMessageMixin, FormView):
    form_class = CustomerImportForm
    template_name = "customer/import.html"
    success_url = "/customer/import/"
    success_message = "Customer successfully imported"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "customer"
        context["child_segment"] = "import"
        return context

    def form_valid(self, form):
        csvfile = form.cleaned_data.get("csvfile", None)
        if csvfile is not None:
            df = pd.read_csv(csvfile)
            df_dict = df.to_dict(orient="index")
            try:
                customer_list = [
                    Customer(
                        citizenship_no=v["citizenship number"],
                        pan_no=v["pan number"],
                        fullname=v["full name"],
                        dob=v["date of birth"],
                        gender=v["gender"],
                        email=v["email"],
                        phone=v["phone"],
                        occupation=v["occupation"],
                        city=v["city"],
                        district=v["district"],
                        state=v["state"],
                        country=v["country"],
                        address=v["address"],
                    )
                    for i, v in df_dict.items()
                ]
            except KeyError:
                form.add_error(
                    None,
                    """Column name in file doesn't match! 
                    Columns: 
                    'citizenship number', 'pan number', 'full name', 'date of birth', 'gender', 'email',
                    'phone', 'occupation', 'city', 'district', 'state', 'country', 'address'.""",
                )
                return self.render_to_response(self.get_context_data(form=form))

            objs = Customer.objects.bulk_create(customer_list)
            pprint(objs)

        return super().form_valid(form)
