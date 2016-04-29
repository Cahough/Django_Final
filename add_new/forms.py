from django import forms
from django.forms import PasswordInput
class add_form(forms.Form):
	username = forms.CharField(label='username',max_length=30)
	password = forms.CharField(label='password',max_length=30, widget=PasswordInput())
	password2 = forms.CharField(label='password2', max_length=30,widget=PasswordInput())
