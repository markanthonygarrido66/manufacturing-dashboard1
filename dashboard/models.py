from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
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

    total_units = models.IntegerField(default=0)
    good_units = models.IntegerField(default=0)
    defective_units = models.IntegerField(default=0)

    yield_percentage = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('manager', 'Manager'),
        ('executive', 'Executive'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)