# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *

# Create your models here.
class QuoteManager(models.Manager):
    def quoteIsValid(self, post):
        creator = post['creator']
        message = post['message']

        errors = []
        if len(creator) < 2 :
             errors.append('Please enter a valid creator of the quote')
        if len(message) < 10 or len(message) > 500:
             errors.append('Quote has to be between 10-500 characters')

        return {'status': len(errors) == 0, 'errors':errors}

    def newQuote(self, post):
        creator = post['creator']
        message = post['message']
        user = int(post['user'])
        # userInt = int(user)
        print user
        user_id = User.objects.get(id=user)
        new_quote = self.create(creator=creator, message=message, user=user_id)
        # new_quote.quotes.add(user_id)
        return new_quote


class Quote(models.Model):
    creator = models.CharField(max_length=100)
    message = models.TextField()
    user = models.ForeignKey(User, related_name="quotes")

    objects = QuoteManager()

    def __str__(self):
        return "creator: {}, message: {}".format(self.creator, self.message)
