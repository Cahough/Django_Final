from django.db import models

class contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_ength=50)


	def __str__(self):
		return self.first_name
#to integrate run: python manage.py makemigrations
#first time run: python manage.py migrate (not neccesary)
# to add to a = contact(first_name = "first", last_name = "last"...)
#to save it to the database a.save()
#to read do contact.objects.all() (returns all objects)
#just returns a list of objects
#can also do a.objects.create(first_name="jane",last_name="doe"...)
#where clause is done as such:
#contact.objects.filter(first_name = "parameter")
#contact.objects.filter(first_name startswith='j')
#contact.objects.filter(first_name contains='J')
#contact.objects.filter(etc).order_by('last_name')
