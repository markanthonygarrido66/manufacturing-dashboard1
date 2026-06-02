from django.urls import path
from . import views
from .views import push_sensor_data
urlpatterns = [
    path('', views.sensor_dashboard, name='sensor_dashboard'),
    path("api/sensors/push/", push_sensor_data, name="push_sensor_data"),
    path('sensors/', views.sensors_view, name='sensors')
]
