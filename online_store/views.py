from django.shortcuts import render

from shopping_carts.models import ShoppingCart
from products.models import Product

from .functions import get_list_with_random_ids


def main_page_view(request):
	template = 'online_store/base.html'
	context = {}
	
	if request.user.is_authenticated():
		request.session['shopping_cart_id'] = request.user.shopping_cart.id
	else:
		shopping_cart = ShoppingCart.objects.create()
		request.session['shopping_cart_id'] = shopping_cart.id

	products = Product.objects.filter(id__in=get_list_with_random_ids(model=Product, count=5))
	context['products'] = products
	return render(request, template, context)


