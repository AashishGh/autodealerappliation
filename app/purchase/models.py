from django.db import models
from django.urls.base import reverse
from django.utils.translation import gettext as _

from vehicle.models import Vehicle

class Purchase(models.Model):
    invoice_no = models.CharField(_("invoice number"), max_length=50, unique=True)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, verbose_name=_("vehicle"))
    purchase_date = models.DateField(_("purchase date"))
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    vendor_name = models.CharField(_("vendor name"), max_length=200)
    vendor_address = models.TextField(_("vendor address"), max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return self.invoice_no

    def get_absolute_url(self):
        return reverse("purchase-detail", kwargs={"id": self.id})