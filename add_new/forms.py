# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# add_new/forms.py

# Defines form creation for adding a new login user.

from django import forms
from django.forms import PasswordInput
class add_form(forms.Form):
	username = forms.CharField(label='username',max_length=30)
	password = forms.CharField(label='password',max_length=30, widget=PasswordInput())
	password2 = forms.CharField(label='password2', max_length=30,widget=PasswordInput())
