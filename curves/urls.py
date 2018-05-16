from django.urls import path, include
from . import views

app_name = 'curves'

height_curves_patterns = [
    path(
        'male-months/',
        views.HeightCurveMaleMonths.as_view(),
        name='height-male-months'
    ),
    path(
        'male-years/',
        views.HeightCurveMaleYears.as_view(),
        name='height-male-years'
    ),
    path(
        'female-months/',
        views.HeightCurveFemaleMonths.as_view(),
        name='height-female-months'
    ),
    path(
        'female-years/',
        views.HeightCurveFemaleYears.as_view(),
        name='height-female-years'
    ),
]

urlpatterns = [
    path(
        'api/growth-curve/height/',
        include(height_curves_patterns)
    ),
]
