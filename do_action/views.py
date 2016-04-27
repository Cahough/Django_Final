from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from list.models import my_contacts
from .forms import input_form

def index(request):
	response = 'the uid is: '+request.POST['uid']
	"""if request.method == 'POST':
		form = input_form(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks/')
	else:
		form = input_form()
	return render(request,'do_action.html',{'form': form})"""
	return HttpResponse(response)

def delete(request):
    first_name = str(request.POST['first_name'])
    last_name = str(request.POST['last_name'])
    email = str(request.POST['email'])
    phone = str(request.POST['phone'])

    list = my_contacts.objects.filter(first__contains=first_name, last__contains=last_name, email__contains=email, phone__contains=phone).delete()
    body = "<h4> Contact sucessfully deleted. </h4>"
    return redirect('http://127.0.0.1:8000/')


def update(request):
    pass

