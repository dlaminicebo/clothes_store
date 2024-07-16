from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    ship_full_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}), required=True)
    ship_email=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}), required=True)
    ship_address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}), required=True)
    ship_address2=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}), required=False)
    ship_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}), required=True)
    ship_province=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Province'}), required=False)
    ship_postalcode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Postal Code'}), required=False)
    ship_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}), required=True)

    class Meta:
        model= ShippingAddress
        fields=['ship_full_name', 'ship_email', 'ship_address1', 'ship_address2', 'ship_city', 'ship_province', 'ship_postalcode', 'ship_country',]

        exclude= ['user',]


