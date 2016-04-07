from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .forms import list_form
#import contact

# Create your views here.
def index(request):
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	statement = 'SELECT * FROM contact'
	c.execute(statement)
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
	response += '<body>'
	temp = 0
	for row in c:
		temp += 1
		response += '<h4>contact: '+str(temp)+'</h4>'
		response += '<form action="do_action" method="post">'
		my_list = str(row).split(',')
		line1 = str(my_list[0])
		line1 = line1.replace('(','')
		line1 = line1.replace("'","")
		line1 = 'First Name: <br><input type=?text? name=?firstname? value=?'+line1+'?> <br>'
		line1 = line1.replace('?','"')
		line2 = str(my_list[1])
		line2 = line2.replace("'","")
		line2 = 'Last Name: <br><input type=?text? name=?lastname? value=?'+line2+'?> <br>'
		line2 = line2.replace('?','"')
		line3 = str(my_list[2])
		line3 = 'Phone: <br><input type=?text? name=?phone? value=?'+line3+'?> <br>'
		line3 = line3.replace('?','"')
		line4 = str(my_list[3])
		line4 = line4.replace("'","")
		line4 = line4.replace(')','')
		line4 = 'Email: <br><input type=?text? name=?email? value=?'+line4+'?> <br>'
		line4 = line4.replace('?','"')
		button1 = '<br><input type=?submit? value=?delete?>'
		button1 = button1.replace('?','"')
		button2 = '<input type=?submit? value=?update?>'
		button2 = button2.replace('?','"')
		response += line1
		response += line2
		response += line3
		response += line4
		response += button1
		response += button2
		response += '</form>'
	response += '</body>'
	conn.commit()
	conn.close()
	return HttpResponse(response)

def detail(request, question_id):
	return HttpResponse("you are looking at question %s" % question_id)

def results(request, question_id):
	response = "you are looking at response %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you are voting for question %s" % question_id)

