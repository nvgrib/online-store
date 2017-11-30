from django.contrib import admin
from shopping_carts.models import ShoppingCartItem, ShoppingCart

class ShoppingCartItemAdmin(admin.ModelAdmin):
	list_display = ['shopping_cart', 'product', 'quantity', 'price']

class ShoppingCartAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'id', 'total_price']

admin.site.register(ShoppingCartItem, ShoppingCartItemAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
