from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^items$', views.items),
    url(r'^items/add$', views.newItem),
    url(r'^items/newitem$', views.addNewItem),
    url(r'^items/deleteitem/(?P<item_id>\d+)$', views.delItem),
    url(r'^items/wishlist/add/(?P<item_id>\d+)$', views.addWishlist),
    url(r'^items/wishlist/rem/(?P<item_id>\d+)$', views.remWishlist),
    url(r'^profiles/(?P<item_id>\d+)$', views.showProfile),
]
