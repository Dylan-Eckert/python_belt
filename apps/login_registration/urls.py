from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_register/login$', views.login),
    url(r'^login_register/registration$', views.registration),
    url(r'^login_register/logout$', views.logout),
]
