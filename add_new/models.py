# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# add_new/models.py

# Creates login class for admin users.

from django.db import models

# Create your models here.
class login_info(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

	def __str__(self):
		temp = self.username+self.password
		return temp
