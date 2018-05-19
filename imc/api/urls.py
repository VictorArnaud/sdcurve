from django.urls import path
from . import views

imc_curves_patterns_api = [
    path(
        'male/',
        views.IMCCurveMale.as_view(),
        name='curve-male'
    ),
    path(
        'female/',
        views.IMCCurveFemale.as_view(),
        name='curve-female'
    ),
    path(
        'result/',
        views.IMCCurveResultView.as_view(),
        name='curve-result'
    )
]
