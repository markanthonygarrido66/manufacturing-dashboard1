from django.urls import path
from . import views

urlpatterns = [
    path('', views.production_home, name='production_home'),
    path(
    "live/",
    views.production_live,
    name="production_live"
),
]