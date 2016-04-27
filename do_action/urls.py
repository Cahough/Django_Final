from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^update/', views.update, name='update'),
    url(r'^delete/', views.delete, name='delete')
]