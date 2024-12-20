"""
URL configuration for restaurant_kitchen_service project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("kitchen.urls", namespace="kitchen")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
