from django.db import models

# Create your models here.
class ProductionLine(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="active")

    def __str__(self):
        return self.name

class ProductionRecord(models.Model):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    production_date = models.DateField()

    output = models.IntegerField(default=0)  # ✅ ADD THIS

    yield_percentage = models.FloatField(default=0)
    defects = models.IntegerField(default=0)