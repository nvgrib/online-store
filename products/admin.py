from django.contrib import admin

from products.models import Product

# add product_description
class ProductAdmin(admin.ModelAdmin):
	fields = ['slug', 'category', 'manufacturer', 'name', 'price', 'image', 'stock', 'description']
	
admin.site.register(Product, ProductAdmin)