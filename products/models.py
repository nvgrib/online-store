from django.db import models

from manufacturers.models import Manufacturer
from categories.models import Category
from shopping_carts.models import ShoppingCart



class Product(models.Model):
	slug = models.SlugField(max_length=10, unique=True, 
		verbose_name='Product code')
	category = models.ForeignKey(Category, related_name='products')
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=100, unique=True)
	price = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='products/images/', blank=True)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	


	def __str__(self):
		return '{} {} {}, {}$'.format(self.category, self.manufacturer, self.name, self.price)

	def url_name(self):
		return self.name.replace(' ', '-')

	def full_name(self):
		return self.category.name + ' ' +self.manufacturer.name + ' ' + self.name
	
