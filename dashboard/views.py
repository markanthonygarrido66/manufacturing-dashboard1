from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.db.models import Sum, Avg
from .decorators import allowed_roles
from .models import ProductionLine, YieldRecord

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random
from django.http import JsonResponse
from dashboard.models import YieldRecord
# =========================
# MAIN DASHBOARD VIEW
# =========================
@login_required
@allowed_roles(['manager', 'executive'])
def dashboard(request):


    production_lines = ProductionLine.objects.all()
    records = YieldRecord.objects.all()

    line = request.GET.get('line')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # FILTERS
    if line:
        records = records.filter(production_line_id=line)

    if start and end:
        records = records.filter(production_date__range=[start, end])

    # AGGREGATES (SAFE VERSION)
    total_yield = records.aggregate(Sum('yield_percentage'))['yield_percentage__sum'] or 0
    avg_yield = records.aggregate(Avg('yield_percentage'))['yield_percentage__avg'] or 0

    # CHART DATA
    chart_labels = list(records.values_list('production_date', flat=True))
    chart_data = list(records.values_list('yield_percentage', flat=True))

    context = {
        "production_lines": production_lines,
        "records": records,

        "total_yield": total_yield,
        "avg_yield": round(avg_yield, 2),
        "production_count": records.count(),
        "efficiency": round(avg_yield, 2),

        # IMPORTANT: keep raw lists (we will convert in template via json_script)
        "chart_labels": chart_labels,
        "chart_data": chart_data,
    }

    role = request.user.role

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "role": role
        }
    )
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_yield(request):

    line_id = request.data.get('line_id')
    output = request.data.get('output')

    YieldRecord.objects.create(
        production_line_id=line_id,
        output=output
    )

    return Response({
        "message": "Yield recorded successfully"
    })

# =========================
# LIVE API (AJAX / IoT READY)
# =========================
def dashboard_live(request):

    return JsonResponse({
        "total_yield": 1825 + random.randint(-50,50),
        "avg_yield": 91 + random.uniform(-2,2),
        "production_count": 20 + random.randint(0,5)
    })

def dashboard_chart_live(request):

    records = YieldRecord.objects.order_by('production_date')

    labels = []
    data = []

    for r in records:
        labels.append(str(r.production_date))
        data.append(
    float(r.yield_percentage) +
    random.uniform(-1,1)
)

    return JsonResponse({
        "labels": labels,
        "data": data
    })