from django.urls import path
from . import views

weight_curves_patterns_api = [
    path(
        'male-months/',
        views.WeightCurveMaleMonths.as_view(),
        name='curve-male-months'
    ),
    path(
        'male-years/',
        views.WeightCurveMaleYears.as_view(),
        name='curve-male-years'
    ),
    path(
        'female-months/',
        views.WeightCurveFemaleMonths.as_view(),
        name='curve-female-months'
    ),
    path(
        'female-years/',
        views.WeightCurveFemaleYears.as_view(),
        name='curve-female-years'
    ),
    path(
        'result/',
        views.WeightCurveResultView.as_view(),
        name='curve-result'
    )
]
