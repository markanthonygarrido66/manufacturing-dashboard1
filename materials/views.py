from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def materials_home(request):
    return render(request, 'materials/materials_home.html')