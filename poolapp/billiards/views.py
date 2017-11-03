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
def win(request):
    if request.method == 'POST':
        outcome_form = forms.OutcomeForm(request.POST, instance=request.user.profile)
        if outcome_form.is_valid():
            outcome_form.save()
            return redirect('index')
    else:
        outcome_form = forms.OutcomeForm(instance=request.user.profile)
    return render(request, 'poolapp/Outcome.html', {
        'outcome_form': outcome_form,
    })  
    
def loss(request):
    if request.method == 'POST':
        outcome_form = forms.OutcomeForm(request.POST, instance=request.user.profile)
        if outcome_form.is_valid():
            outcome_form.save()
            return redirect('index')
    else:
        outcome_form = forms.OutcomeForm(instance=request.user.profile)
    return render(request, 'poolapp/Outcome.html', {
        'outcome_form': outcome_form,
    })  
    
       
def update_challenger(request):
    if request.method == 'POST':
        challenger_form = forms.ChallengerForm(request.POST, instance=request.user.profile)
        if challenger_form.is_valid():
            challenger_form.save()
            return redirect('index')
    else:
        challenger_form = forms.ChallengerForm(instance=request.user.profile)
    return render(request, 'poolapp/EnterRank.html', {
        'challenger_form': challenger_form,
    })  
    
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
