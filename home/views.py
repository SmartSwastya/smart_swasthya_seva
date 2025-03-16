### views.py
from django.shortcuts import render
from .models import HomeModel

def index(request):
    homes = HomeModel.objects.all()
    return render(request, 'home/index.html', {'homes': homes})