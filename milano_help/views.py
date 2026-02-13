@"
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
"@ | Out-File -Encoding UTF8 views.py
