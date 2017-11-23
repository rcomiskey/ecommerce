from django.conf.urls import url
from .views import viewproducts, do_search

urlpatterns = [
 url(r'^$', viewproducts, name='viewproducts'),
 url(r'^search/', do_search, name='search')
 
]

   