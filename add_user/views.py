from django.shortcuts import render
from django.http import HttpResponse
from .forms import input_form
import sqlite3

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = input_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = input_form()
	return render(request,'name.html',{'form': form})

def calc(request):
	def clean_phone(my_phone):
		temp = ''
		x = 0
		while x < 20 and x < len(my_phone):
			if my_phone[x].isdigit():
				temp += my_phone[x]
			x += 1
		return temp

	def clean_name(my_string):
		temp = ''
		x = 0
		while x < 20 and x < len(my_string):
			if my_string[x].isalpha():
				temp += my_string[x]
			x += 1
		return temp

	def clean_email(my_string):
		temp = ''
		temp = my_string.replace("'","")
		if len(my_string) > 50:
			temp = temp[0:20]
		return temp

	first = clean_name(str(request.POST['first_name']))
	last = clean_name(str(request.POST['last_name']))
	email = clean_email(str(request.POST['email']))
	phone = clean_phone(str(request.POST['phone']))
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	statement = "INSERT INTO contact(first,last,phone,email) Values( '"
	statement = statement+first+"', '" +last+"', "+phone+", '"+email+"' )"
	c = conn.cursor()
	c.execute(statement)
	conn.commit()
	conn.close()
	return HttpResponse(statement)
