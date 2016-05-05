# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# models.py

# Defines primary functions for homepage.

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from .forms import login_form
from list.models import login_info
import hashlib

def index(request):
	if request.method =='POST':
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = login_form()
	return render(request,'login.html', {'form': form})

def home(request):
	uname = request.POST['username']
	passw = request.POST['password']
	object = hashlib.sha256(passw.encode())
	passw = object.hexdigest()
	list = login_info.objects.filter(username = uname)
	if len(list) > 0:
		for l in list:
			if passw == l.password:
				return render_to_response('home.html')
			else:
				return render(request, 'incorrect.html',{'username':uname})
	else:
		return render(request, 'incorrect.html',{'username':"none"})
