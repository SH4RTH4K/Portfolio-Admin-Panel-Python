from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # this will load your index.html
    path('contact/', views.contact, name='contact'),
]