from django.shortcuts import render

from .models import Category


def all_categories(request):
	template = 'categories/all_categories.html'
	categories = Category.objects.all()
	context = {'categories': categories}
	return render(request, template, context) 



