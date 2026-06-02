from django.db import models

class MaterialRecord(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name