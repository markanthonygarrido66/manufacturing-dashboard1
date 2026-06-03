from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductionRecord
import random

def production_home(request):
    records = ProductionRecord.objects.order_by('-production_date')

    return render(
        request,
        'production/production_home.html',
        {
            'records': records
        }
    )


def production_live(request):

    records = ProductionRecord.objects.order_by('-production_date')

    total_output = sum(r.yield_percentage for r in records)

    daily_production = random.randint(80, 150)

    efficiency = random.randint(85, 99)

    rows = []

    for r in records[:10]:

        rows.append({
            "line": r.production_line.name,
            "output": round(
                r.yield_percentage + random.randint(-2, 2),
                2
            ),
            "date": str(r.production_date)
        })

    data = {
        "total_output": round(total_output, 2),
        "daily_production": daily_production,
        "efficiency": efficiency,
        "records": rows
    }

    return JsonResponse(data)