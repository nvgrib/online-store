from django.db import models




class ShoppingCartItem(models.Model):
	shopping_cart = models.ForeignKey('ShoppingCart', related_name='shopping_cart_items')
	product = models.ForeignKey('products.Product', related_name='shopping_cart_items')
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return '{}, {} х {}'.format(self.shopping_cart.__str__, self.product.name, self.quantity)

	def price(self):
		return self.product.price * self.quantity



class ShoppingCart(models.Model):

	def __str__(self):
		rep_str = ''
		rep_str += '{} shopping cart'.format(self.id)
		return rep_str
		

	def total_price(self):
		tot_price = 0
		for i in self.shopping_cart_items.all():
			tot_price += i.price()
		return tot_price


