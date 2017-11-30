from django import forms
from django.conf import settings

from core.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'birthday', 'first_name', 'last_name']


class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']