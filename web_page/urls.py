# Alex Martinez, Carter Hough, Kevin Chlopek
# 05.05.16
# CS 310 - Python
# Django Project
# urls.py

# Defines primary urls for various app functions such as searching, adding new user, adding new contact, editing, deleting, etc.

"""web_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
import web_page.views
import list.views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', web_page.views.index, name="login"),
	url(r'^home/',web_page.views.home, name="home"),
	url(r'^add_new/',include('add_new.urls')),
	url(r'^list/',include('list.urls')),
	url(r'^add/', include('add_user.urls')),
	url(r'^search/', include('search.urls')),
	url(r'^do_action/', include('do_action.urls')),
	#url(r'^admin/', admin.site.urls),
]
