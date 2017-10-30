from django.shortcuts import render


def index(request):
    return render(request, 'poolapp/index.html')