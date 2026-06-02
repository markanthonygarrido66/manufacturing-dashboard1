from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from dashboard import views
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
    
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    )),
    path('logout/', LogoutView.as_view(), name='logout'),
   path('dashboard/', include('dashboard.urls')),
    path('production/', include('production.urls')),
    path('materials/', include('materials.urls')),
    path('sensors/', include('sensors.urls')),
    
]