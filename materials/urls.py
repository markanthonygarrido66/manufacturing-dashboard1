from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials_home, name='materials_home'),
    path(
    "live/",
    views.materials_live,
    name="materials_live"
),
]