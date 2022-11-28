from django import forms
from .models import Product


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label="Quantité")
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
    
class ProductForm(forms.ModelForm):
 

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "price",
            "image",
        ]    