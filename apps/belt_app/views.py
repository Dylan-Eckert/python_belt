# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from ..login_registration.models import User

# Create your views here.
# ===============================================
#                     VIEWS
# ===============================================
def index(request):
    return redirect('/items')

def showProfile(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    item = Item.objects.get(id = item_id)

    data = {
    'item':item,
    }

    return render(request, 'belt_app/profile.html', data)

def items(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    user = User.objects.get(id=request.session['user_id'])
    items = Item.objects.exclude(wishlisted=user)

    data = {
    'user': user,
    'items':items,
    }

    return render(request, 'belt_app/items.html', data)

def addNewItem(request):
    return render(request, 'belt_app/addNewitem.html')

# ===============================================
#                   PROCESSES
# ===============================================

def newItem(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    res = Item.objects.itemIsValid(request.POST)
    if res['status']:
        item = Item.objects.newItem(request.POST, request.session['user_id'])
    else:
        for error in res['errors']:
            messages.error(request, error)
        return redirect('/items/newitem')
    return redirect('/items')

def addWishlist(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Item.objects.addWishlist(item_id, request.session['user_id'])
    return redirect('/items')

def remWishlist(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Item.objects.remWishlist(item_id, request.session['user_id'])
    return redirect('/items')

def delItem(request, item_id):
    Item.objects.delItem(item_id)
    return redirect('/items')
