from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login),
    url(r'^index/$',views.index),
    url(r'^status/$',views.status),
    url(r'^lnr$',views.lnr),
]
