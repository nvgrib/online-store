from django.shortcuts import render
from django.views import generic

from shopping_carts.views import add_shopping_cart_item
from comments.forms import CommentForm
from comments.models import Comment

from .models import Product


class AllProducts(generic.ListView):
	template_name = 'products/all_products.html'
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.all()


def one_category_products(request, category_name):
	template = 'products/one_category_products.html'
	products = Product.objects.filter(category__name__iexact=category_name)
	context = {'products': products}
	return render(request, template, context)


# Should I take category_name parameter?
# I have doubts about 'get' method.
def product_details(request, category_name, product_name):
	template = 'products/product_details.html'
	product = Product.objects.get(name__iexact=product_name.replace('-', ' '))
	comment_form = CommentForm()
	comments = Comment.objects.filter(product__id=product.id).order_by('-created')
	context = {'product': product, 'comment_form': comment_form, 'comments': comments}

	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		
		if comment_form.is_valid():
			user = request.user
			Comment.objects.create(user=user, product=product, text=comment_form.cleaned_data['text'])

		if request.POST.get('add_to_cart'):
			add_shopping_cart_item(request, product.id)

	return render(request, template, context)




