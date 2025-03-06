from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart_quantity']  # Only include the quantity field

    cart_quantity = forms.IntegerField(
        min_value=1,
        max_value=999,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'quantity',  # Add id for targeting the input
        })
    )