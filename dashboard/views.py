from django.shortcuts import render
from .models import ProductionLine, YieldRecord

def dashboard_view(request):

    production_lines = ProductionLine.objects.all()

    records = YieldRecord.objects.all()

    line = request.GET.get('line')

    if line:
        records = records.filter(
            production_line_id=line
        )

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'production_lines': production_lines,
            'records': records
        }
    )