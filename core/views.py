from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from core.models import User
from core.forms import UserForm, UserLoginForm
from shopping_carts.models import ShoppingCart, ShoppingCartItem


def registration_user_view(request):
	template = 'core/registration_user.html'
	context = {}
	user_form = UserForm()

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			shopping_cart = ShoppingCart.objects.create()
			User.objects.create_user(shopping_cart=shopping_cart, **user_form.cleaned_data)
			return HttpResponseRedirect('/')
	
	context['user_form'] = user_form
	return render(request, template, context)


def login_user_view(request):
	template = 'core/login_user.html'
	context = {}
	user_login_form = UserLoginForm()

	if request.method == 'POST':
		shopping_cart_id = request.session['shopping_cart_id']
		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			move_shopping_cart_items_from_anonymous_user_to_user(request, shopping_cart_id)
			return HttpResponseRedirect('/')
		else:
			user_login_form = UserLoginForm({'username':request.POST['username']})
			messages.info(request, 'Username or password is incorrect')

	context['user_login_form'] = user_login_form
	return render(request, template, context)


def move_shopping_cart_items_from_anonymous_user_to_user(request, shopping_cart_id):
	shopping_cart_id = shopping_cart_id
	user_shopping_cart_id = request.user.shopping_cart.id
	request.session['shopping_cart_id'] = user_shopping_cart_id

	anonymous_user_shopping_cart_item__product_ids = {item.product.id for item in ShoppingCartItem.objects.filter(
			shopping_cart_id=shopping_cart_id)}
	user_shopping_cart_item__product_ids = {item.product.id for item in ShoppingCartItem.objects.filter(
			shopping_cart_id=user_shopping_cart_id)}
	union = anonymous_user_shopping_cart_item__product_ids - user_shopping_cart_item__product_ids
	
	ShoppingCartItem.objects.filter(
		shopping_cart__id=shopping_cart_id
						   ).filter(
		product__id__in=union
						   ).update(
		shopping_cart_id=user_shopping_cart_id)


def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


def profile_view(request):
	template = 'core/profile.html'
	context = {}

	context['user_form'] = UserForm()
	return render(request, template, context)