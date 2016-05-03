from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^update/', views.update, name='update'),
	url(r'^delete/([0-9])', views.delete, name='delete'),
	#url(r'^delete/(?P<uid>[0-9]+)/$', views.delete, name='delete')
	#url(r'^delete/(?P<student_id>[0-9]+)/$', views.delete, name='delete')
]
