from django.conf.urls import url
from . import views

urlpatterns = [
	#this is passing to views.py
    url(r'^$', views.index ),
    url(r'^register', views.register ),
    url(r'^travels$', views.login ),
    url(r'^travels/add$', views.add),
    url(r'^travels/dashboard$', views.create_trip),



    # url(r'^travel', views.travel ),
    # url(r'^traveldetails', views.travel ),
]