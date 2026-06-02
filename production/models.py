from django.db import models

# Create your models here.
class ProductionLine(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="active")


class ProductionRecord(models.Model):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    production_date = models.DateField()
    yield_percentage = models.FloatField()
    defects = models.IntegerField(default=0)