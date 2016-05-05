# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# list/urls.py

# Defines urls for showing on contacts based on different sort-by fields.

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^first_name/',views.first_name, name='first_name'),
    url(r'^last_name/',views.last_name, name='last_name'),
    url(r'^by_phone/',views.by_phone, name='by_phone'),
    url(r'^by_email/',views.by_email, name='by_email'),
]
