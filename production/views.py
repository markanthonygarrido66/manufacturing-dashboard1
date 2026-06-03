from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductionRecord
import random
from django.db.models import Sum
from django.utils.timezone import localdate

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

    today = localdate()

    today_records = ProductionRecord.objects.filter(production_date=today)

    total_output = records.aggregate(total=Sum("output"))["total"] or 0

    daily_production = today_records.aggregate(total=Sum("output"))["total"] or 0

    efficiency = (daily_production / 200) * 100 if daily_production else 0

    rows = []

    for r in records[:10]:
        rows.append({
            "line": r.production_line.name,
            "output": r.output,
            "date": str(r.production_date)
        })

    return JsonResponse({
        "total_output": total_output,
        "daily_production": daily_production,
        "efficiency": round(efficiency, 2),
        "records": rows
    })