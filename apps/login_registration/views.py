# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
# ===================================================
#                      RENDER
# ===================================================

def index(request):
    return render(request, 'login_registration/index.html')

# ===================================================
#                    PROCESSES
# ===================================================
def login(request):
    user = User.objects.login(request.POST)
    if user:
        request.session['user_id'] = user.id
        return redirect('/')

    messages.error(request, 'Email or Password invalid')
    return redirect('/login_register/')

def registration(request):
    res = User.objects.userIsValid(request.POST)
    if res['status']:
        user = User.objects.newUser(request.POST)
        request.session['user_id'] = user.id
        return redirect('/')
    else:
        for error in res['errors']:
            messages.error(request, error)

    return redirect('/login_register/')

def logout(request):
    request.session.clear()

    return redirect('/login_register/')
