from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class ShippingAddress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ship_full_name=models.CharField(max_length=255)
    ship_email=models.CharField(max_length=255)
    ship_address1=models.CharField(max_length=255)
    ship_address2=models.CharField(max_length=255,null=True, blank=True)
    ship_city=models.CharField(max_length=255)
    ship_province=models.CharField(max_length=255, null=True, blank=True)
    ship_postalcode=models.CharField(max_length=255, null=True, blank=True)
    ship_country=models.CharField(max_length=255)

    #Don't pluralize address
    class Meta:
        verbose_name_plural="Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
    
