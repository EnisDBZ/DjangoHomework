from django import forms
from .models import CartItem,UserAddress

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

class UserAddressForm(forms.ModelForm):
    address_title = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Adres Başlığı'}), required=False)
    full_address = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Adres'}), required=False)
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Şehir'}), required=False)
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'İl'}), required=False)
    state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'İlçe'}), required=False)
    postal_code = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Posta Kodu'}), required=False)
    phone = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefon'}), required=False)
    is_default = forms.BooleanField(label="Varsayılan Olarak Ayarlansın mı ?",widget=forms.CheckboxInput(attrs={'class':'form-control','placeholder':''}), required=False)

    class Meta:
        model = UserAddress
        fields= (
            'address_title',
            'full_address',
            'country',
            'city',
            'state',
            'postal_code',
            'phone',
            'is_default'
        )
