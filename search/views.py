# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# search/views.py

# Defines functions for performing a search for a contact in the address book.

from django.shortcuts import render
from django.http import HttpResponse
from .forms import search_form
from list.models import my_contacts
# Create your views here.

def index(request):
	if request.method =='POST':
		form = search_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = search_form()
	return render(request,'search/search.html', {'form': form})

def do_search(request):
	first_name = str(request.POST['first_name'])
	last_name = str(request.POST['last_name'])
	_email = str(request.POST['email'])
	_phone = str(request.POST['phone'])
	list = my_contacts.objects.filter(first__contains=first_name, last__contains=last_name, email__contains=_email, phone__contains=_phone)
	events = []
	for l in list:
		x = []
		x.append(l.id)
		x.append(l.first)
		x.append(l.last)
		x.append(l.email)
		x.append(l.phone)
		events.append(x)
	return render(request, 'search/do_search.html',{'events':events})
