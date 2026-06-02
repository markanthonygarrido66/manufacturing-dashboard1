from django.urls import path
from . import views

urlpatterns = [
    path('', views.production_home, name='production_home'),
]