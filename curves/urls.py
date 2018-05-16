from django.urls import path, include
from .api import urls

app_name = 'curves'

urlpatterns = [
    path(
        'api/growth-curve/height/',
        include(urls.height_curves_patterns_api)
    ),
]
