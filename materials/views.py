from django.http import JsonResponse
from .models import MaterialRecord
from django.shortcuts import render

def materials_home(request):
    return render(request, 'materials/materials_home.html')

def materials_live(request):

    materials = MaterialRecord.objects.all()

    data = []

    for m in materials:

        data.append({
            "name": m.name,
            "stock": m.stock_quantity
        })

    return JsonResponse(data, safe=False)