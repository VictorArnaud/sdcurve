from django.urls import path, include
from .api import urls

app_name = 'imc'

urlpatterns = [
    path(
        'api/growth-curve/imc/',
        include(urls.imc_curves_patterns_api)
    ),
]
