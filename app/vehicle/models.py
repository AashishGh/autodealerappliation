from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls.base import reverse
from django.db import models
from django.utils.translation import gettext as _

class Vehicle(models.Model):
    vehicle_model = models.CharField(_("vehicle model"), max_length=100)
    color =  models.CharField(_("color"), max_length=100)
    chasis_no =  models.CharField(_("chasis number"), max_length=100)
    engine_no =  models.CharField(_("engine number"), max_length=100)
    reg_no = models.CharField(_("registration number"), max_length=100, unique=True)
    key_no =  models.CharField(_("key number"), max_length=20, blank=True, default="None")
    battery_no =  models.CharField(_("battery number"), max_length=100)
    mfd_year = models.PositiveIntegerField(_("mfd year"), validators=[MinValueValidator(2000), MaxValueValidator(2050)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        constraints = [
            models.UniqueConstraint(fields=['chasis_no', 'engine_no'], name="unique_vehicle")
        ]

    def __str__(self):
        return f"{self.chasis_no} {self.engine_no}"

    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={"id": self.id})