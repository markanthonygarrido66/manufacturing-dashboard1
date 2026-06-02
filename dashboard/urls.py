from django.urls import path
from . import views
from .views import push_yield
from .api_views import push_yield

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/yield/', push_yield),
    path("dashboard/live/", views.dashboard_live, name="dashboard_live"),
    path('api/push-yield/', views.push_yield, name='push_yield'),
]