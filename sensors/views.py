from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import render
from .models import SensorData


# =========================
# SENSOR DASHBOARD PAGE
# =========================
def sensor_dashboard(request):
    """
    UI page (browser dashboard)
    """
    context = {
        "temperature": 28,
        "humidity": 60,
        "pressure": 101.3,
    }

    return render(request, "sensors/sensor_dashboard.html", context)


# =========================
# IoT SENSOR API (JWT READY)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_sensor_data(request):
    """
    API endpoint for IoT devices
    """

    data = request.data

    # basic validation (important for IoT stability)
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    pressure = data.get("pressure")

    if temperature is None or humidity is None or pressure is None:
        return Response(
            {"error": "Missing sensor data"},
            status=400
        )

    sensor = SensorData.objects.create(
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
    )

    return Response({
        "message": "Data received successfully",
        "sensor_id": sensor.id
    })

def sensors_view(request):
    return render(request, "sensors/sensor_dashboard.html")