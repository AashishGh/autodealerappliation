from django import forms

from vehicle.models import Vehicle
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    invoice_no = forms.CharField(
        max_length=50,
        required=True,
        label="Invoice Number:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        required=True,
        label="Vehicle Purchased:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    purchase_date = forms.DateField(
        required=True,
        label="Purchase Date:",
        widget=forms.TextInput(
            attrs={
                "class": "custom-control",
                "type": "date",
            },
        ),
    )

    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label="Price Incl. VAT:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    vendor_name = forms.CharField(
        max_length=200,
        required=True,
        label="Vendor Name:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    vendor_address = forms.CharField(
        max_length=300,
        required=True,
        label="Vendor Address:",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
    )

    class Meta:
        model = Purchase
        fields = "__all__"


from .validators import FileValidator


class PurchaseImportForm(forms.Form):
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



