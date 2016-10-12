from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',auth_views.login,{'template_name':'huiu/login.html'}),
    url(r'^index/$',views.index),
]
