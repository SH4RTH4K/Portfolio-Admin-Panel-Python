from django.shortcuts import render, redirect
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact
from django.contrib import messages

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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        fingerprint = request.POST.get('fingerprint')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0].strip()

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            ip_address=ip_address,
            fingerprint=fingerprint
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')

    return render(request, 'index.html')