from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from .models import SensorData


# =========================
# SENSOR DASHBOARD UI
# =========================
@login_required(login_url='/login/')
def sensor_dashboard(request):
    context = {
        "temperature": 28,
        "humidity": 60,
        "pressure": 101.3,
    }
    return render(request, "sensors/sensor_dashboard.html", context)


# =========================
# IoT API (JWT READY)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_sensor_data(request):

    data = request.data

    temperature = data.get("temperature")
    humidity = data.get("humidity")
    pressure = data.get("pressure")

    if temperature is None or humidity is None or pressure is None:
        return Response({"error": "Missing sensor data"}, status=400)

    sensor = SensorData.objects.create(
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
    )

    return Response({
        "message": "Data received successfully",
        "sensor_id": sensor.id
    })

def sensors_live(request):

    latest = SensorData.objects.order_by(
        "-id"
    ).first()

    if not latest:

        return JsonResponse({
            "temperature": 0,
            "humidity": 0,
            "pressure": 0
        })

    return JsonResponse({
        "temperature": latest.temperature,
        "humidity": latest.humidity,
        "pressure": latest.pressure
    })