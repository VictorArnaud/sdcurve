from django.views.generic import TemplateView
from .examples import Constants
from .models import HeightCurve


class PlotHeightCurveView(TemplateView):
    """
    View to plot a height curve.
    """

    template_name = "curves/height.html"

    def make_curves(self, graphic):
        """
        Function to create percentis curves to plot.
        """

        array_data_table = [['Ages', '3%', '10%', '25%', '50%', '75%', '90%', '97%']]

        ages = graphic.make(HeightCurve.AGES)
        percentis_3 = graphic.make(HeightCurve.PERCENTIS_3)
        percentis_10 = graphic.make(HeightCurve.PERCENTIS_10)
        percentis_25 = graphic.make(HeightCurve.PERCENTIS_25)
        percentis_50 = graphic.make(HeightCurve.PERCENTIS_50)
        percentis_75 = graphic.make(HeightCurve.PERCENTIS_75)
        percentis_90 = graphic.make(HeightCurve.PERCENTIS_90)
        percentis_97 = graphic.make(HeightCurve.PERCENTIS_97)

        for age in ages:
            array_data_table.append([
                ages[age],
                percentis_3[age],
                percentis_10[age],
                percentis_25[age],
                percentis_50[age],
                percentis_75[age],
                percentis_90[age],
                percentis_97[age],
            ])

        return array_data_table

    def get_context_data(self, **kwargs):
        """
        Insert data to plot the graphic.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        context = super(PlotHeightCurveView, self).get_context_data(**kwargs)

        context['graphic'] = self.make_curves(graphic)
        return context
