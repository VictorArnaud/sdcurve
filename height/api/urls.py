from django.urls import path
from . import views

height_curves_patterns_api = [
    path(
        'male-months/',
        views.HeightCurveMaleMonths.as_view(),
        name='curve-male-months'
    ),
    path(
        'male-years/',
        views.HeightCurveMaleYears.as_view(),
        name='curve-male-years'
    ),
    path(
        'female-months/',
        views.HeightCurveFemaleMonths.as_view(),
        name='curve-female-months'
    ),
    path(
        'female-years/',
        views.HeightCurveFemaleYears.as_view(),
        name='curve-female-years'
    ),
    path(
        'result/',
        views.HeightCurveResultView.as_view(),
        name='curve-result'
    )
]
