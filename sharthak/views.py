from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):
    context = {
        'home': Home.objects.latest('updated'),
        'about': About.objects.latest('updated'),
        'profiles': Profile.objects.all(),
        'categories': Category.objects.all(),
        'skills': Skills.objects.all(),
        'portfolio': Portfolio.objects.all(),
    }
    return render(request, 'index.html', context)