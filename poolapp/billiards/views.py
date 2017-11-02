from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import forms


def index(request):
    current_user = request.user
    user_id = current_user.id
    user=User.objects.get(pk=user_id)
    return render(request, 'poolapp/index.html',{'user':user})
    
    
@login_required
@transaction.atomic

def update_profile(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            
            return redirect('index')
        
            
    else:
        user_form = forms.UserForm(instance=request.user)
    return render(request, 'poolapp/EnterRank.html', {
        'user_form': user_form,
    })
