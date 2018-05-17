from django.urls import path, include
from .api import urls
from . import views

app_name = 'height'

height_curves_patterns = [
    path(
        '',
        views.PlotHeightCurveView.as_view(),
        name='plot-curve'
    )
]

urlpatterns = [
    path(
        'growth-curve/height/',
        include(height_curves_patterns)
    ),
    path(
        'api/growth-curve/height/',
        include(urls.height_curves_patterns_api)
    ),
]
