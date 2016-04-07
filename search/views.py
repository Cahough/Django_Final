from django.shortcuts import render
from django.http import HttpResponse
from .forms import search_form
import sqlite3

# Create your views here.

def index(request):
	if request.method =='POST':
		form = search_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = search_form()
	return render(request,'search.html', {'form': form})

def do_search(request):
	return HttpResponse("doing search")
