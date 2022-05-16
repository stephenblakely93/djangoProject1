from django import forms
from .models import Customer


class CustomerChoiceField(forms.Form):

    customers = forms.ModelChoiceField(
        queryset=Customer.objects.values_list("customer_name", flat=True).distinct(), empty_label=None
    )


