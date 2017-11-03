from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from . import forms


def index(request):
    current_user = request.user
    user_id = current_user.id
    user=User.objects.get(pk=user_id)
    return render(request, 'poolapp/index.html',{'user':user,'table': Profile.objects.all})
    
    
@login_required
@transaction.atomic

def update_profile(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    else:
        user_form = forms.UserForm(instance=request.user.profile)
    return render(request, 'poolapp/EnterRank.html', {
        'user_form': user_form,
    })
def leaderboard(request):
    return render(request, 'poolapp/EnterRank.html', {
        'user_form': user_form,
    })
