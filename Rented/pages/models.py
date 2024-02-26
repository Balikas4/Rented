from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Listing(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index = True)
    description = models.TextField(_("description"), blank=True, max_length = 100000)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index = True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index = True)
    is_available = models.BooleanField(_("is available"), db_index = True, default = False)
    brand = models.CharField(_("brand"), max_length=100, db_index = True)
    owner = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("owner"), 
        on_delete=models.CASCADE,
        related_name = 'listings',
        )

    class Meta:
        verbose_name = _("listing")
        verbose_name_plural = _("listings")
        ordering = ['is_available', 'created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("listing_detail", kwargs={"pk": self.pk})
