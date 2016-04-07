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
	response = ''
	temp = 0
	for row in c:
		temp += 1
		my_list = str(row).split(',')
		line1 = 'first: '+str(my_list[0])+'<br>'
		line1 = line1.replace('(','')
		line1 = line1.replace("'","")
		line2 = 'last: '+str(my_list[1])+'<br>'
		line2 = line2.replace("'","")
		line3 = 'phone: '+str(my_list[2])+'<br>'
		line4 = 'email: '+str(my_list[3])+'<br>'
		line4 = line4.replace("'","")
		line4 = line4.replace(')','')
		response += '<h4>contact: '+str(temp)+'</h4>' 
		response += line1
		response += line2
		response += line3
		response += line4
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

