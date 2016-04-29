from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import add_form
from list.models import login_info

def index(request):
	if request.method == 'POST':
		form = add_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = add_form()
	return render(request,'add_new.html',{'form': form})

def do_add(request):
	uname = request.POST['username']
	pass1 = request.POST['password']
	pass2 = request.POST['password2']
	if pass1 == pass2:
		list = login_info.objects.all()
		my_id = len(list) + 1
		a = login_info(id=my_id,username=uname,password=pass_)
		a.save()
		return redirect('http://127.0.0.1:8000/add_new/')
	else:
		return render(request, 'not_same.html', {'password1':pass1, 'password2':pass2})
