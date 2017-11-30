from django.conf import settings
from django.conf.urls import url, include	
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from . import views


app_name = 'online_store'


urlpatterns = [
    url(r'^$', views.main_page_view, name='main_page_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^category/', include('categories.urls', namespace='categories')),
    url(r'^', include('core.urls')),
    url(r'^', include('shopping_carts.urls')),
    url(r'^', include('comments.urls')),
]

urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)