from django.urls import path
from . import views
from .views import push_yield
from .api_views import push_yield

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/yield/', push_yield),
]