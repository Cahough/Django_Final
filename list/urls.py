from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^do_action',views.do_action, name='do_action'),
]
