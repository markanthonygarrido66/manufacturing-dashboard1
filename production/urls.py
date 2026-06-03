from django.urls import path
from . import views

urlpatterns = [
    path('', views.production_home, name='production_home'),
    path(
    "live/",
    views.production_live,
    name="production_live"
),
path("production/input/", views.production_input_page),
path("api/production/input/", views.production_input_api),
 path('input/', views.production_input_page, name='production_input_page'),
    path('api/input/', views.production_input_api, name='production_input_api'),
]
