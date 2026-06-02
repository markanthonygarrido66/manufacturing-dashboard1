from django.shortcuts import render

def sensor_dashboard(request):
    return render(request, 'sensors/sensor_dashboard.html')