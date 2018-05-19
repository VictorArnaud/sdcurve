from django.urls import path
from . import views

perimeter_curves_patterns_api = [
    path(
        'male/',
        views.PerimeterCurveMale.as_view(),
        name='curve-male'
    ),
    path(
        'female/',
        views.PerimeterCurveFemale.as_view(),
        name='curve-female'
    ),
    path(
        'result/',
        views.PerimeterCurveResultView.as_view(),
        name='curve-result'
    )
]
