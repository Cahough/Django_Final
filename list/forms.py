from django import forms

class list_form(forms.Form):
        first_name = forms.CharField(label='first name',max_length=30)
        last_name = forms.CharField(label='last name',max_length=30)
        email = forms.CharField(label='email',max_length=30)
        phone = forms.CharField(label='phone',max_length=30)