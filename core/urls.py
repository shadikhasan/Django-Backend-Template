from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # Optional
    path('api/', include('myapp.urls')),     # Backend API endpoints
]
