from django import forms
from vehicle.models import Vehicle
from scheme.models import Scheme
from customer.models import Customer
from .models import Sale, PaymentMode


class SaleForm(forms.ModelForm):
    invoice_no = forms.CharField(
        max_length=50,
        required=True,
        label="Invoice Number:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    challan_no = forms.CharField(
        max_length=50,
        required=True,
        label="Delivery Challan Number:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        required=True,
        label="Vehicle:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=True,
        label="Customer:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    sale_date = forms.DateField(
        required=True,
        label="Sale Date:",
        widget=forms.TextInput(
            attrs={
                "class": "custom-control",
                "type": "date",
            },
        ),
    )

    amount = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label="Price Incl. VAT:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    discount = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=False,
        label="Discount:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    payment_mode = forms.ChoiceField(
        choices=PaymentMode.choices,
        required=True,
        label="Payment Mode:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    scheme = forms.ModelChoiceField(
        queryset=Scheme.objects.all(),
        required=True,
        label="Scheme:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    finance_amount = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=False,
        label="Finance Amount:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    exchange_amount = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=False,
        label="Exchange Amount:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Sale
        fields = "__all__"


from .validators import FileValidator


class SaleImportForm(forms.Form):
    validate_file = FileValidator(
        max_size=26214400,
        content_types=(
            "text/comma-separated-values",
            "application/csv",
            "text/csv",
            "application/excel",
            "application/vnd.ms-excel",
            "application/vnd.msexcel",
            "text/plain",
        ),
    )

    csvfile = forms.FileField(
        allow_empty_file=False,
        required=True,
        widget=forms.widgets.ClearableFileInput(
            attrs={"class": "custom-file custom-file-control", "accept": ".csv"}
        ),
        validators=[
            validate_file,
        ],
    )
