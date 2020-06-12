from django import forms

from .models import Pay


class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ['description', 'amount']
        widgets = {
            'userName': forms.HiddenInput(),
            'password': forms.HiddenInput(),
            'orderNumber': forms.HiddenInput(),
            'returnUrl': forms.HiddenInput()
        }
