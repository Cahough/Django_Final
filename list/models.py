from django.db import models

# Create your models here.
class Contacts(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	phone = models.IntegerField()
