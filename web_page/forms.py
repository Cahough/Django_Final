from django import forms

class login_form(forms.Form):
	username = forms.CharField(label='user name',max_length=30)
	password = forms.CharField(label='password',max_length=30)
