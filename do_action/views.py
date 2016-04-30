# to start you need to make a form in the index filling out the parts of the
# form with the first name, last name, phone, and email. from there you 
# need to put two buttons on the html page that this page will use as
# a template. to see an example look at the template called add.html
# it will look very similar. you will need to make the actions of those
# buttons to be "delete/" and "update/". On the delete portion you will
# want to retrieve the information from the form like you are already doing
# however instead of doing x.save you will do x.delete(). Also the way it 
# is set up now it could delete a contact that is similar to the name entered
# to fix this you will need to remove the contains portion of the object filter
# and make sure that it must be equal to the user.

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

    x = my_contacts.objects.filter(first=first_name, last=last_name, email=email, phone=phone)
    x.delete()

    #contact = my_contacts.objects.get(pk=uid)
    #contact.delete()
    body = "<h4> Contact sucessfully deleted. </h4>"
    #HttpResponseRedirect('http://127.0.0.1:8000/', response)
    return redirect('http://127.0.0.1:8000/')


def update(request):
    pass

