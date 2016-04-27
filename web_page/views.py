from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .forms import login_form

def index(request):
	if request.method =='POST':
		form = login_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = login_form()
	return render(request,'login.html', {'form': form})

def home(request):
	return render_to_response('home.html')
