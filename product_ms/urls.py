"""
URL configuration for product_ms project.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("user.urls")),
    path("", include("product.urls")),
]
