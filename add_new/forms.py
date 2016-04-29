from django import forms

class add_form(forms.Form):
	username = forms.CharField(label='username',max_length=30)
	password = forms.CharField(label='password',max_length=30)
	password2 = forms.CharField(label='password2', max_length=30)
