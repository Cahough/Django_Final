# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# do_action/urls.py

# Defines url for editing and deleting a contact.

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^delete/', views.delete, name='delete'),
	url(r'^update/', views.update, name='update'),
]
