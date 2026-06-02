from django.contrib import admin
from .models import ProductionLine, YieldRecord

admin.site.register(ProductionLine)
admin.site.register(YieldRecord)