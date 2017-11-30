from django import forms


class ProductIdForm(forms.Form):
	product_id = forms.CharField(max_length=5)

class ShoppingCartItemIdForm(forms.Form):
	shopping_cart_item_id = forms.CharField(max_length=5)