from django import forms
from .models import Scheme


class SchemeForm(forms.ModelForm):
    scheme_name = forms.CharField(
        max_length=300,
        required=True,
        label="Scheme Name:",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )

    description = forms.CharField(
        max_length=500,
        required=False,
        label="Description:",
        widget=forms.widgets.Textarea(attrs={"class": "form-control", "rows": "5"}),
    )

    class Meta:
        model = Scheme
        fields = "__all__"


from .validators import FileValidator


class SchemeImportForm(forms.Form):
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
