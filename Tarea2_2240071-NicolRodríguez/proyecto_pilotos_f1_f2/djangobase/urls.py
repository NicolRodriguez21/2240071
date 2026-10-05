"""
URL configuration for djangobase project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('modulo.urls')),
    path('admin/', admin.site.urls),
]
