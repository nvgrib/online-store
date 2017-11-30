from .models import ShoppingCart, ShoppingCartItem


def del_shopping_cart_item(shopping_cart_item_id):
	ShoppingCartItem.objects.get(id=shopping_cart_item_id).delete()