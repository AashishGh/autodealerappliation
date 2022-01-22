from django import forms
from .models import Vehicle
from datetime import date

class VehicleForm(forms.ModelForm):

    def getYearChoices(start_year: int, last_year: int):
        return [( str(i), i ) for i in range(start_year, last_year, -1 )]

    vehicle_model = forms.CharField(
        max_length=100,
        required=True,
        label= "Vehicle Model:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    color = forms.CharField(
        max_length=100,
        required=True,
        label= "Color:",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    chasis_no = forms.CharField(
        max_length=100,
        required=True,
        label="Chasis Number:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    engine_no = forms.CharField(
        max_length=100,
        required=True,
        label="Engine Number:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    reg_no = forms.CharField(
        max_length=100,
        required=True,
        label="Registration Number:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    key_no = forms.CharField(
        max_length=20,
        required=True,
        label="Key Number:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    mfd_year = forms.IntegerField(
        min_value=2000,
        max_value=2100,
        required=True,
        label="MFD Year:",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            },
        ))

    battery_no = forms.CharField(
        max_length=100,
        required=True,
        label="Battery Number:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = Vehicle 
        fields = "__all__"



from .validators import FileValidator


class VehicleImportForm(forms.Form):
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

