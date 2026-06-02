from django.shortcuts import render

def sensor_dashboard(request):
    context = {
        "temperature": 28,
        "humidity": 60,
        "pressure": 101.3,
    }
    return render(request, "sensors/sensor_dashboard.html", context)