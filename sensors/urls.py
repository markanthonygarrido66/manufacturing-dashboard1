from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_dashboard, name='sensor_dashboard'),
    path('api/push/', views.push_sensor_data, name='push_sensor_data'),
    path('sensors/', views.sensor_dashboard, name='sensor_dashboard')
]