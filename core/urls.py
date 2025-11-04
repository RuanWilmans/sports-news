"""
core/urls.py

Project URL configuration: admin + news app.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
]
