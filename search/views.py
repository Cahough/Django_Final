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
	return render(request,'search.html', {'form': form})

def do_search(request):
	response = ''
	response += """<style>
		.button-container form,
		.button-container form div{
        		display: inline;
		}

		.button-container button {
        		display: inline;
        		vertical-align: middle;
		}
		</style>
		<h1>put in what you know and press search</h1>
		<div class="button-container">
		<form action="http://127.0.0.1:8000/search">
        		<div>
                		<button type="submit"> search page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000/add">
        		<div>
                		<button type="submit">add page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000">
        		<div>
                		<button type="submit">home page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000/list">
        		<div>
                		<button type="submit">show contacts</button>
        		</div>
		</form>
		</div>"""
	first_name = str(request.POST['first_name'])
	last_name = str(request.POST['last_name'])
	_email = str(request.POST['email'])
	_phone = str(request.POST['phone'])
	list = my_contacts.objects.filter(first__contains=first_name, last__contains=last_name, email__contains=_email, phone__contains=_phone)
	response +='<body><br><br>'
	for l in list:
		response +='FIRST: '+l.first
		response += '<br>'
		response +='LAST: '+l.last
		response += '<br>'
		response += 'EMAIL: '+l.email
		response +='<br>'
		response += 'PHONE: '+str(l.phone)+'<br>'+'<br>'
	response += '</body>'
	return HttpResponse(response)
