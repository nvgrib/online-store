from django.db import models
from core.models import User
from products.models import Product


class Comment(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product, related_name='comments')
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}, {}, {}'.format(self.user, self.product, self.created)


class CommentLike(models.Model):
	user = models.ForeignKey(User)
	comment = models.ForeignKey(Comment, related_name='likes')
	created = models.DateTimeField(auto_now_add=True)
