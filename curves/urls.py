from django.urls import path, include
from . import views
from .api import urls

app_name = 'curves'

height_curves_patterns = [
    path(
        '',
        views.PlotHeightCurveView.as_view(),
        name='height-curve'
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
