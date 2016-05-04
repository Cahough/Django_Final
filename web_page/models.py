from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class login_info(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

	def __str__(self):
		temp_string = self.username
		temp_string += self.password
		return temp_string

