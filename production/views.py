from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductionRecord
import random


def production_home(request):
    return render(request, 'production/production_home.html')


def production_live(request):

    records = ProductionRecord.objects.order_by('-production_date')[:10]

    data = []

    for r in records:
        data.append({
            "line": r.production_line.name,
            "output": r.yield_percentage + random.randint(-2, 2),
            "date": str(r.production_date)
        })

    return JsonResponse(data, safe=False)