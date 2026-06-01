from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'api/token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view()
    ),
    path('dashboard', include('dashboard.urls')),
    path(
    '',
    auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ),
    name='login'
),
]