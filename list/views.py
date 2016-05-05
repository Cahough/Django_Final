# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# list/views.py

# Defines functions for showing all contacts in address book.

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
    events=[]
    for l in list:
        x=[]
        x.append(l.id)
        x.append(l.first)
        x.append(l.last)
        x.append(l.email)
        x.append(l.phone)
        events.append(x)
    return render(request, 'list.html',{'events':events})

def first_name(request):
    list = my_contacts.objects.order_by('first')
    events=[]
    for l in list:
        x=[]
        x.append(l.id)
        x.append(l.first)
        x.append(l.last)
        x.append(l.email)
        x.append(l.phone)
        events.append(x)
    return render(request, 'list.html',{'events':events})

def last_name(request):
    list = my_contacts.objects.order_by('last')
    events=[]
    for l in list:
        x=[]
        x.append(l.id)
        x.append(l.first)
        x.append(l.last)
        x.append(l.email)
        x.append(l.phone)
        events.append(x)
    return render(request, 'list.html',{'events':events})

def by_phone(request):
    list = my_contacts.objects.order_by('phone')
    events=[]
    for l in list:
        x=[]
        x.append(l.id)
        x.append(l.first)
        x.append(l.last)
        x.append(l.email)
        x.append(l.phone)
        events.append(x)
    return render(request, 'list.html',{'events':events})

def by_email(request):
    list = my_contacts.objects.order_by('email')
    events=[]
    for l in list:
        x=[]
        x.append(l.id)
        x.append(l.first)
        x.append(l.last)
        x.append(l.email)
        x.append(l.phone)
        events.append(x)
    return render(request, 'list.html',{'events':events})
