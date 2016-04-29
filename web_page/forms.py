from django import forms
from django.forms import PasswordInput

class login_form(forms.Form):
	username = forms.CharField(label='user name',max_length=30)
	password = forms.CharField(label='password',max_length=30,widget=PasswordInput())
