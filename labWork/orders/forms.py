from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    preferred_datetime = forms.DateTimeField(
        label="Желаемая дата и время",
        widget=forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'})
    )

    class Meta:
        model = Order
        fields = ['address', 'contact_phone','service_type','preferred_datetime', 'payment_type']

        widgets={
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-select'}),
            'payment_type': forms.Select(attrs={'class': 'form-select'}),
        }
    