from django.conf.urls import url, include	

from core import views


app_name = 'core'


urlpatterns = [
	url(r'^registration/$', views.registration_user_view, name='registration_user_view'),
	url(r'^login/$', views.login_user_view, name='login_user_view'),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^profile/$', views.profile_view, name='profile_view'),

]