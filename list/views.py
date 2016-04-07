from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h1>list</h1>")

def detail(request, question_id):
	return HttpResponse("you are looking at question %s" % question_id)

def results(request, question_id):
	response = "you are looking at response %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you are voting for question %s" % question_id)

