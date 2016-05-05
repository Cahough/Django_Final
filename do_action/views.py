# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# do_action/views.py

# Defines update and delete functions for editing and deleting a contact.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from list.models import my_contacts
from .forms import input_form

def index(request):
    first, last, phone, email = "", "", "", ""
    uid = 0
    response = 'the uid is: '+request.POST['uid']
    contact = my_contacts.objects.filter(id=request.POST['uid'])
    for c in contact:
        first=c.first
        last=c.last
        phone=c.phone
        email=c.email
        uid=c.id
        print(first+last+str(phone)+email)
    return render(request,'do_action.html',{'uid':uid,'first_name': first, 'last_name':last, 'phone':phone, 'email':email})

def delete(request):
    uid = str(request.POST['uid'])
    x = my_contacts.objects.filter(id=uid)
    x.delete()
    return redirect('http://127.0.0.1:8000/list/')

def update(request):
    x = my_contacts.objects.filter(id=str(request.POST['uid']))
    first_ = str(request.POST['first_name'])
    last_ = str(request.POST['last_name'])
    email_ = str(request.POST['email'])
    phone_ = str(request.POST['phone'])
    for contact in x:
        contact.first = first_
        contact.last = last_
        contact.email = email_
        contact.phone = phone_
        contact.save()
    return redirect('http://127.0.0.1:8000/list/')