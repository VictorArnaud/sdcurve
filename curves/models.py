from curves.examples import Constants
from curves.examples.height_curves import (
    HeightCurveMaleYears, HeightCurveMaleMonths,
    HeightCurveFemaleYears, HeightCurveFemaleMonths
)


class HeightCurve(object):
    """
    Growth curve based on the height of the child with Down Syndrome.
    """

    def __init__(self, gender=Constants.MALE, age=Constants.YEARS):
        """
        Redirects to chart type according to past parameters, MALE or FEMALE
        genre, and age MONTHS or YEARS
        """

        self.graphic = []

        if gender == Constants.MALE and age == Constants.YEARS:
            curve = HeightCurveMaleYears()
        elif gender == Constants.MALE and age == Constants.MONTHS:
            curve = HeightCurveMaleMonths()
        elif gender == Constants.FEMALE and age == Constants.YEARS:
            curve = HeightCurveFemaleYears()
        else:
            curve = HeightCurveFemaleMonths()

        self.graphic = curve.make()

    def make(self):
        """
        Return a graphic
        """

        return self.graphic
