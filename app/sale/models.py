from django.db import models
from django.db.models.deletion import CASCADE
from django.urls.base import reverse
from django.utils.translation import gettext as _

from scheme.models import Scheme
from customer.models import Customer
from vehicle.models import Vehicle


class PaymentMode(models.TextChoices):
    CASH = "Cash"
    CHEQUE = "Cheque"
    E_BANKING = "E-Banking"
    CASH_CHEQUE = "Cash and Cheque"
    CASH_E_BANKING = "Cash and E-Banking"
    CHEQUE_E_BANKING = "Cheque and E-Banking"
    CASH_CHEQUE_E_BANKING = "Cash, Cheque and E-Banking"


class Sale(models.Model):

    invoice_no = models.CharField(_("invoice number"), max_length=50, unique=True)
    challan_no = models.CharField(_("challan number"), max_length=50)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=CASCADE, verbose_name=_("vehicle")
    )
    customer = models.ForeignKey(
        Customer, on_delete=CASCADE, verbose_name=_("customer")
    )
    sale_date = models.DateField(_("sale date"))
    amount = models.DecimalField(_("amount"), max_digits=8, decimal_places=2)
    discount = models.DecimalField(
        _("discount"),
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0.00,
    )
    payment_mode = models.CharField(
        _("payment mode"), max_length=50, choices=PaymentMode.choices
    )
    scheme = models.ForeignKey(Scheme, on_delete=CASCADE, verbose_name=_("scheme"))
    finance_amount = models.DecimalField(
        _("finance amount"),
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0.00,
    )
    exchange_amount = models.DecimalField(
        _("exchange amount"),
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0.00,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return self.invoice_no

    def get_absolute_url(self):
        return reverse("sale-detail", kwargs={"id": self.id})
