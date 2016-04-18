from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import input_form
from list.models import my_contacts

# Test comment from Carter to make sure git is set up properly
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = input_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = input_form()
	return render(request,'add.html',{'form': form})

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

	first_name = clean_name(str(request.POST['first_name']))
	last_name = clean_name(str(request.POST['last_name']))
	_email = clean_email(str(request.POST['email']))
	_phone = clean_phone(str(request.POST['phone']))
	a = my_contacts(first=first_name,last=last_name,email=_email,phone=int(_phone))
	a.save()
	body = "<h4> your information has been successfully added</h4>"
	return redirect('http://127.0.0.1:8000/')
