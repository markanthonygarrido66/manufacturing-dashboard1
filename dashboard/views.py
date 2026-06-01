from django.shortcuts import render
from .models import ProductionLine, YieldRecord
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@login_required
@allowed_roles(['manager', 'executive'])
def dashboard(request):

    production_lines = ProductionLine.objects.all()
    records = YieldRecord.objects.all()

    line = request.GET.get('line')
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')

    if line:
        records = records.filter(production_line_id=line)

    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])

    return render(request, 'dashboard/dashboard.html', {
        'production_lines': production_lines,
        'records': records
    })
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_yield(request):

    line_id = request.data.get('line_id')
    output = request.data.get('output')

    YieldRecord.objects.create(
        production_line_id=line_id,
        output=output
    )

    return Response({"message": "Yield recorded"})