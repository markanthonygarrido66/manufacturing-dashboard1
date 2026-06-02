from django.db import models
from django.contrib.auth.models import User

class ProductionLine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class YieldRecord(models.Model):
    production_line = models.ForeignKey(
        ProductionLine,
        on_delete=models.CASCADE
    )

    production_date = models.DateField()

    total_units = models.IntegerField()

    good_units = models.IntegerField()

    defective_units = models.IntegerField()

    yield_percentage = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('manager', 'Manager'),
        ('executive', 'Executive'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)