from django.db import models

# Create your models here.
ROLE_CHOICES = (
    ('worker', 'Worker'),
    ('manager', 'Manager'),
    ('boss', 'Boss'),
)

role = models.CharField(
    max_length=20,
    choices=ROLE_CHOICES,
    default='worker'
)