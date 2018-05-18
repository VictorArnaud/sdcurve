from django.views.generic import TemplateView
from core import Constants
from .models import HeightCurve


class PlotHeightCurveView(TemplateView):
    """
    View to plot a height curve.
    """

    template_name = "height/curves.html"

    def get_context_data(self, **kwargs):
        """
        Insert data to plot the graphic.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        context = super(PlotHeightCurveView, self).get_context_data(**kwargs)

        context['graphic'] = graphic.make_charts()
        return context
