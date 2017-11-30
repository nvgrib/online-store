from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'products'


urlpatterns = [
	url(r'^(?P<category_name>[\w\s]+)/$', views.one_category_products, name='one_category_products'),
	url(r'^(?P<category_name>[\w\s]+)/(?P<product_name>[\w\s\,\-\\/]+)$', views.product_details, name='product_details'),
]


