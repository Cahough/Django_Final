from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^first_name/',views.first_name, name='first_name'),
url(r'^last_name/',views.last_name, name='last_name'),
url(r'^by_phone/',views.by_phone, name='by_phone'),
url(r'^by_email/',views.by_email, name='by_email'),
]
