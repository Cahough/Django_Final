from django.shortcuts import render
from django.http import HttpResponse
from .forms import list_form
from list.models import my_contacts
#import contact

# Create your views here.
def index(request):
	response = """	<style>
			.button-container form,
			.button-container form div{
        			display: inline;
			}

			.button-container button {
        			display: inline;
        			vertical-align: middle;
			}
			</style>
			<h1>this is a list of all your contacts</h1>
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
	response += '<body><br><br><br>'
	for object in my_contacts.objects.all():
		response += 'FIRST: '+str(object.first)
		response += '<br>'
		response += 'LAST: '+str(object.last)
		response += '<br>'
		response += 'EMAIL: '+str(object.email)
		response += '<br>'
		response += 'PHONE: '+str(object.phone)
		response += '<br><br>'
	response += '</body>'
	return HttpResponse(response)

def do_action(request):
	first = str(request.POST['firstname'])
	last = str(request.POST['lastname'])
	email = str(request.POST['email'])
	phone = str(request.POST['phone'])
	respone = first.last.email.phone
	return HttpResponse(response)



