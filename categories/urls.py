from django.conf.urls import url, include

from . import views


app_name = 'categories'


urlpatterns = [
	url(r'^all/$', views.all_categories, name='all_categories'),
	url(r'^', include('products.urls', namespace='products')),
]