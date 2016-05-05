# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# add_new/urls.py

# Defines url for creating a new admin user.

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^do_add/', views.do_add, name='do_add'),
]
