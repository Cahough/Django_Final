# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# list/models.py

# Defines classes for accessing contact info and for login authentication.

from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class my_contacts(models.Model):
	first = models.CharField(max_length=20)
	last = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	phone = models.IntegerField()

	def __str__(self):
		temp_string = self.first
		temp_string += self.last
		temp_string += self.email
		temp_string += str(self.phone)
		return temp_string

class login_info(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

	def __str__(self):
		temp = self.username+self.password
		return temp
