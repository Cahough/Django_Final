from django.db import models

# Create your models here.
Class my_users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	
	def __str__(self):
		temp_string = self.first
		temp_string += self.last
		return temp_string

