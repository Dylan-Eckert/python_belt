# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *

# Create your models here.
class ItemManager(models.Manager):
    def itemIsValid(self, post):
        item = post['item']

        errors = []
        if len(item) < 2 :
             errors.append('Please enter a valid item')

        return {'status': len(errors) == 0, 'errors':errors}

    def newItem(self, post, userid):
        name = post['item']
        user = User.objects.get(id=userid)
        new_item = self.create(name=name, user=user)
        new_item.wishlisted.add(user)
        return new_item

    def delItem(self, itemid):
        return Item.objects.filter(id=itemid).delete()

    def addWishlist(self, itemid, userid):
        if Item.objects.filter(id=itemid).exists():
            user = User.objects.get(id=userid)
            item = Item.objects.get(id=itemid)
            user.wishlist.add(item)

    def remWishlist(self, itemid, userid):
        if Item.objects.filter(id=itemid).exists():
            user = User.objects.get(id=userid)
            item = Item.objects.get(id=itemid)
            user.wishlist.remove(item)


class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="items")
    wishlisted = models.ManyToManyField(User, related_name="wishlist", default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ItemManager()

    def __str__(self):
        return "name: {}".format(self.name)
