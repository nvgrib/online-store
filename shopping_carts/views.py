from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from products.models import Product

from .models import ShoppingCart, ShoppingCartItem
from .forms import ProductIdForm, ShoppingCartItemIdForm


def shopping_cart_view(request):
	template = 'shopping_carts/shopping_cart.html'
	context = {}
	
	shopping_cart_items = ShoppingCartItem.objects.filter(
		shopping_cart__id=request.session['shopping_cart_id'])
	if shopping_cart_items:
		context['shopping_cart_items'] = shopping_cart_items
	else:
		messages.info(request, 'Your shopping cart is empty')

	return render (request, template, context)


def add_shopping_cart_item(request, product_id):
	product = Product.objects.get(id=product_id)
	shopping_cart = ShoppingCart.objects.get(id=request.session['shopping_cart_id'])
	
	try:
		ShoppingCartItem.objects.filter(shopping_cart__id=request.session['shopping_cart_id']
			).get(product__id=product_id)

	except ObjectDoesNotExist:
		ShoppingCartItem.objects.create(
					shopping_cart=shopping_cart, 
					product=product,
		)	
	else:
		messages.warning(request, 'You already own this product in your shopping cart')
	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def payment_for_shopping_cart_items(request):
	if request.user.is_authenticated:
		shopping_cart_items = ShoppingCartItem.objects.filter(
			shopping_cart__id=request.session['shopping_cart_id'])
		for item in shopping_cart_items:
			try:
				product = item.product
				product.stock -= item.quantity
				product.save()
			except IntegrityError:
				messages.warning(request, 'Not enough items in stock')
				return HttpResponseRedirect(reverse('shopping_carts:shopping_cart_view'))
			else:
				shopping_cart_items.delete()
				return HttpResponseRedirect(reverse('shopping_carts:successful_payment_view'))
	else:
		return HttpResponseRedirect(reverse('core:login_user_view'))


def successful_payment_view(request):
	template = 'shopping_carts/successful_payment.html'
	contex = {}

	messages.success(request, 'Payment made successfully')
	return render(request, template, contex)


def delete_shopping_cart_item(request, shopping_cart_item_id):
	ShoppingCartItem.objects.get(id=shopping_cart_item_id).delete()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])



