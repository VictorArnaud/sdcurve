from django.urls import path, include
from .api import urls

app_name = 'perimeter'

urlpatterns = [
    path(
        'api/growth-curve/perimeter/',
        include(urls.perimeter_curves_patterns_api)
    ),
]
