# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# add_user/urls.py

# Defines url for adding new contact info.

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^calc/', views.calc, name='calc')
]
