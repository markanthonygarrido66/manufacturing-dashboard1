from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials_home, name='materials_home'),
]