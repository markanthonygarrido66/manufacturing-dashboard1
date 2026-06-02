from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductionRecord
import random


def production_home(request):
    return render(request, 'production/production_home.html')


from django.http import JsonResponse
from .models import ProductionRecord

def production_live(request):

    records = ProductionRecord.objects.all()

    total_output = 0

    for r in records:
        total_output += r.yield_percentage

    daily_production = random.randint(80, 150)

    efficiency = random.randint(85, 99)

    data = {
        "total_output": round(total_output, 2),
        "daily_production": daily_production,
        "efficiency": efficiency
    }

    return JsonResponse(data)