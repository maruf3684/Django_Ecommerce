
from django import forms
from shop.models.customer_model import Customer

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','city','locality','zipcode','phone_number','division']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'}),
        }
