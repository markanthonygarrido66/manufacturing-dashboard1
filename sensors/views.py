from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SensorData
from django.shortcuts import render

def sensor_dashboard(request):
    context = {
        "temperature": 28,
        "humidity": 60,
        "pressure": 101.3,
    }
    return render(request, "sensors/sensor_dashboard.html", context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_sensor_data(request):
    data = request.data

    sensor = SensorData.objects.create(
        temperature=data.get("temperature"),
        humidity=data.get("humidity"),
        pressure=data.get("pressure"),
    )

    return Response({
        "message": "Data received",
        "id": sensor.id
    })