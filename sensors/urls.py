from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_dashboard, name='sensor_dashboard'),
]
