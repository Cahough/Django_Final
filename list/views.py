from django.shortcuts import render
from django.http import HttpResponse
from .forms import list_form
from list.models import my_contacts
from django import forms
from django.forms.formsets import formset_factory
from list.forms import *

# Create your views here.
def index(request):
	list = my_contacts.objects.all()	
	#my_formset = formset_factory(list_form, extra=len(list))
	#data = {'first':'alex','last':'martinez','email':'email','phone':3033333333}
	#formset=my_formset(data)
	#if request.method == "POST":
		#formset = my_formset(request.POST)
		#if formset.is_valid():
			#message="thank you"
		#else:
		#	message = "something is wrong"
	data = '<h1>list of contacts</h1><body>'
	#data += '<a href="http://127.0.0.1:8000/last_order'
        #data += '">last</a>'
        #data += '<a href="heep://127.0.0.1:800/first_order' 
        #data += '"first</a>'
	for l in list:
		temp = '<a href="http://do_action/'
		temp += str(l.id)+'">'
		temp += l.last + ', '+l.first+'</a> <br><br>'
		data += temp
		print(temp)
	return HttpResponse(data)

"""def first_order(request):
	list = my_contacts.objects.orderby("first")

	data = '<h1>list of contacts</h1><body>'

	#data += '<a href="http://127.0.0.1:8000/last_order'
        #data += '">last</a>'
        #data += '<a href="heep://127.0.0.1:800/first_order' 
        #data += '">first</a>'

        for l in list:
                temp = '<a href="http://do_action/'
                temp += str(l.id)+'">'
                temp += l.first + ', '+l.last+'</a> <br><br>'
                data += temp
                print(temp)
        return HttpResponse(data)


def last_order(request):
	list = my_contacts.objects.all()

        data = '<h1>list of contacts</h1><body>'
	#data += '<a href="http://127.0.0.1:8000/last_order'
	#data += '">last</a>'
	#data += '<a href="heep://127.0.0.1:800/first_order'
	#data += '">first</a>'
        for l in list:
                temp = '<a href="http://do_action/'
                temp += str(l.id)+'">'
                temp += l.last + ', '+l.first+'</a> <br><br>'
                data += temp
                print(temp)
        return HttpResponse(data)

def show grades(request):
	


"""
