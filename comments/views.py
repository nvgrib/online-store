from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Comment, CommentLike
from products.models import Product


def add_remove_like(request, comment_id):
	product = Comment.objects.get(id=comment_id).product
	
	if request.user.is_authenticated:
		try:
			comment_like = CommentLike.objects.get(
				user=request.user, 
				comment__id=comment_id,
			)
		except ObjectDoesNotExist:
			comment = Comment.objects.get(id=comment_id)
			CommentLike.objects.create(user=request.user, comment=comment)
		else:
			comment_like.delete()
	else:
		messages.info(request, 'You need to be a registered user.')

	return HttpResponseRedirect(
		reverse('categories:products:product_details', 
			kwargs={'category_name': product.category, 
		    	    'product_name': product.name,
			}
		)
	)


	
