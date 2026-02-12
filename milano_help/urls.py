from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from core.views import register  # 👈 collega la view register

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('register/', register),  # 👈 questa è la rotta per la registrazione
]
