from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('food.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
]
