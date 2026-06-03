from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('worker', 'Worker'),
    ('manager', 'Manager'),
    ('boss', 'Boss'),
)

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='worker'
    )