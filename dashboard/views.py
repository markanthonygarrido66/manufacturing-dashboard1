from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.db.models import Sum, Avg
from .decorators import allowed_roles
from .models import ProductionLine, YieldRecord


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

    return render(request, "dashboard/dashboard.html", context)


# =========================
# LIVE API (AJAX / IoT READY)
# =========================
def dashboard_live(request):

    line = request.GET.get("line")

    records = YieldRecord.objects.all()

    if line:
        records = records.filter(production_line_id=line)

    data = {
        "total_yield": records.aggregate(Sum('yield_percentage'))['yield_percentage__sum'] or 0,
        "avg_yield": records.aggregate(Avg('yield_percentage'))['yield_percentage__avg'] or 0,
        "production_output": records.count(),
        "material_used": 400  # placeholder (pwede mo palitan later)
    }

    return JsonResponse(data)