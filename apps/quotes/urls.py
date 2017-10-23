from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^quotes$', views.quotes),
    url(r'^quotes/add$', views.addQuote),
    url(r'^profiles/(?P<user_id>[0-9]+)$', views.showProfile),
]
