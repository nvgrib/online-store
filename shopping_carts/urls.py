from django.conf.urls import url, include	
from . import views

app_name = 'shopping_carts'

urlpatterns = [
	url(r'^shopping-cart/$', views.shopping_cart_view, name='shopping_cart_view' ),
	url(r'^add-shopping-cart-item/(?P<product_id>[\w]+)$', views.add_shopping_cart_item, name='add_shopping_cart_item' ),
	url(r'^payment-for-shopping-cart-items/$', views.payment_for_shopping_cart_items, name='payment_for_shopping_cart_items' ),
	url(r'^successful-payment/$', views.successful_payment_view, name='successful_payment_view'),
	url(r'^delete-shopping-cart-item/(?P<shopping_cart_item_id>[\w]+)$', views.delete_shopping_cart_item, name='delete_shopping_cart_item' ),
]