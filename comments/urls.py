from django.conf.urls import url, include

from . import views


app_name = 'comments'

urlpatterns = [
	url(r'^add_remove_like/(?P<comment_id>[\d]+)/$', views.add_remove_like, name='add_remove_like')
]