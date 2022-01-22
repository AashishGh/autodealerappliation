import mimetypes
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .models import Customer, District, State, Gender


class CustomerForm(forms.ModelForm):
    citizenship_no = forms.CharField(
        max_length=50,
        required=True,
        label="Citizenship Number:",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )

    pan_no = forms.CharField(
        max_length=50,
        label="PAN Number:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    fullname = forms.CharField(
        max_length=200,
        required=True,
        label="Customer Name:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    dob = forms.DateField(
        label="Date of Birth:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "custom-control",
                "type": "date",
            },
        ),
    )

    gender = forms.ChoiceField(
        choices=Gender.choices,
        required=True,
        label="Gender:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    email = forms.EmailField(
        max_length=254,
        required=True,
        label="Email:",
        widget=forms.widgets.EmailInput(attrs={"class": "form-control"}),
    )

    phone = forms.CharField(
        max_length=20,
        required=True,
        label="Phone:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    occupation = forms.CharField(
        max_length=200,
        required=True,
        label="Occupation:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    city = forms.CharField(
        max_length=200,
        required=True,
        label="City:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    district = forms.ChoiceField(
        choices=District.choices,
        label="District:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    state = forms.ChoiceField(
        choices=State.choices,
        label="State:",
        widget=forms.Select(attrs={"class": "custom-select"}),
    )

    country = forms.CharField(
        max_length=50,
        required=True,
        label="Country:",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    address = forms.CharField(
        max_length=500,
        required=True,
        label="Address:",
        widget=forms.Textarea(attrs={"rows": "4", "class": "form-control"}),
    )

    class Meta:
        model = Customer
        fields = (
            "citizenship_no",
            "pan_no",
            "fullname",
            "dob",
            "gender",
            "email",
            "phone",
            "occupation",
            "city",
            "district",
            "state",
            "country",
            "state",
            "address",
        )

    # # check if any errors occur here
    # def save(self, commit: bool = ...):
    #     firstname = self.cleaned_data["firstname"]
    #     middlename = self.cleaned_data["middlename"]
    #     surname = self.cleaned_data["surname"]
    #     if middlename:
    #         fullname = f"{firstname} {middlename} {surname}"
    #     else:
    #         fullname = f"{firstname} {surname}"
    #     self.fullname = fullname
    #     return super().save(commit)


from .validators import FileValidator


class CustomerImportForm(forms.Form):
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
            attrs={
                "class": "custom-file custom-file-control",
                "accept": ".csv"
            }
        ),
        validators=[
            validate_file,
        ],
    )
