# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# search/urls.py

# Defines url to perform a search for a contact in the address book.

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^do_search/', views.do_search, name='do_search')
]
