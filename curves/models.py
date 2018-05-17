from curves.examples import Constants
from curves.examples.height_curves import (
    HeightCurveMaleYears, HeightCurveMaleMonths,
    HeightCurveFemaleYears, HeightCurveFemaleMonths
)


class HeightCurve(object):
    """
    Growth curve based on the height of the child with Down Syndrome.
    """

    ALL = 0
    AGES = 1
    PERCENTIS_3 = 2
    PERCENTIS_10 = 3
    PERCENTIS_25 = 4
    PERCENTIS_50 = 5
    PERCENTIS_75 = 6
    PERCENTIS_90 = 7
    PERCENTIS_97 = 8
    TITLE = 9

    def __init__(self, gender=Constants.MALE, age=Constants.YEARS):
        """
        Redirects to chart type according to past parameters, MALE or FEMALE
        genre, and age MONTHS or YEARS
        """

        self.graphic = {}

        if gender == Constants.MALE and age == Constants.YEARS:
            self.curve = HeightCurveMaleYears()
        elif gender == Constants.MALE and age == Constants.MONTHS:
            self.curve = HeightCurveMaleMonths()
        elif gender == Constants.FEMALE and age == Constants.YEARS:
            self.curve = HeightCurveFemaleYears()
        else:
            self.curve = HeightCurveFemaleMonths()

        self.graphic = self.curve.make()

    def make(self, axis=0):
        """
        Return a graphic
        """

        result = []

        if axis == self.ALL:
            result = self.graphic
        elif axis == self.AGES:
            result = self.curve.ages
        elif axis == self.PERCENTIS_3:
            result = self.curve.percentis_3
        elif axis == self.PERCENTIS_10:
            result = self.curve.percentis_10
        elif axis == self.PERCENTIS_25:
            result = self.curve.percentis_25
        elif axis == self.PERCENTIS_50:
            result = self.curve.percentis_50
        elif axis == self.PERCENTIS_75:
            result = self.curve.percentis_75
        elif axis == self.PERCENTIS_90:
            result = self.curve.percentis_90
        elif axis == self.PERCENTIS_97:
            result = self.curve.percentis_97
        else:
            result = self.curve.title

        return result

    def result(self, height, age):
        """
        Check the chart if the child is above, below or at the mean height.
        """

        success = False
        result = 0
        count = 0

        for curve_age in self.curve.ages:
            if age == curve_age:
                success = True
                break

            count += 1

        if not success:
            result = "Idade invalida."
            return result

        if height < self.curve.percentis_3[count]:
            result = -1

        if height > self.curve.percentis_97[count]:
            result = 1

        return result
