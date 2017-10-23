# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from ..login_registration.models import User, UserManager

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    users = User.objects.all()
    data = {'users': users}

    return render(request, 'quotes/index.html', data)

def showProfile(self, user_id):
    user = User.objects.get(id = user_id)
    data = {'user':user}

    return render(self, 'quotes/profile.html', data)

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    users = User.objects.all()
    quotes = Quote.objects.all()
    data = {
    'users': users,
    'quotes':quotes
    }

    return render(request, 'quotes/quotes.html', data)

def addQuote(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')
    quote = Quote.objects.newQuote(request.POST)
    # if request.POST == 'POST':
    #     res = Quote.objects.quoteIsValid(request.POST)
    #     if res['status']:
            # quote = Quote.objects.newQuote(request.POST)
        # else:
        #     for error in res['errors']:
        #         messages.error(request, error)
    return redirect('/quotes')
