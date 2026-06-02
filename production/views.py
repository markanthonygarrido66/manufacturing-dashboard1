from django.shortcuts import render

def production_home(request):
    return render(request, 'production/production_home.html')