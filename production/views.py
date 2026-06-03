from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductionRecord, ProductionLine
import random
from django.db.models import Sum
from django.utils.timezone import localdate
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.timezone import now
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



@csrf_exempt
def production_input_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        line_name = data.get("line")
        output = int(data.get("output"))
        yield_percentage = int(data.get("yield"))
        defects = int(data.get("defects"))

        line, _ = ProductionLine.objects.get_or_create(name=line_name)

        record = ProductionRecord.objects.create(
            
            production_line=line,
            production_date=now().date(),
            output=output,
            yield_percentage=yield_percentage,
            defects=defects
        )
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
    "live_system",
    {
        "type": "send_update",
        "data": {
            "refresh": True
        }
    }
)
        print("🚀 INPUT RECEIVED:", data)

        return JsonResponse({
            "status": "success",
            "id": record.id
        })
    

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

def production_input_page(request):
    return render(request, "production/production_input.html")
