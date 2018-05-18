from django.urls import path, include
from .api import urls

app_name = 'weight'

urlpatterns = [
    path(
        'api/growth-curve/weight/',
        include(urls.weight_curves_patterns_api)
    ),
]
