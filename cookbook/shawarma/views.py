from django.shortcuts import render

from .models import Shawarma

def home(request):
    shawarmas = Shawarma.objects.all()
    return render(request, 'home.html', {
        'shawarmas': shawarmas,
    })
