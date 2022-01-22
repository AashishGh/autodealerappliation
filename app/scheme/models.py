from django.db import models
from django.db.models.fields import CharField, TextField
from django.urls.base import reverse
from django.utils.translation import gettext as _


class Scheme(models.Model):
    scheme_name = CharField(_("scheme name"),unique=True, max_length=200)
    description = TextField(_("description"), max_length=500, blank=True, default="No description")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Scheme"
        verbose_name_plural = "Schemes"

    def __str__(self):
        return self.scheme_name

    def get_absolute_url(self):
        return reverse("scheme-detail", kwargs={"id": self.id})
