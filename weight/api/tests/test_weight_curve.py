from rest_framework.test import APITestCase
from core import Constants
from weight.models import WeightCurve
from weight.curves import (
    WeightCurveMaleYears, WeightCurveMaleMonths,
    WeightCurveFemaleYears, WeightCurveFemaleMonths
)


class WeightCurveTestCase(APITestCase):
    """
    Unit test of weight-based growth curve
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.male_years = WeightCurveMaleYears().make()
        self.male_months = WeightCurveMaleMonths().make()
        self.female_years = WeightCurveFemaleYears().make()
        self.female_months = WeightCurveFemaleMonths().make()

    def test_weight_curve_male_months(self):
        """
        Test to verify if graphic construct is correct with MALE and MONTHS.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )
        self.assertEqual(
            graphic.make(),
            self.male_months
        )
        self.assertEqual(
            graphic.make(WeightCurve.TITLE),
            self.male_months['title']
        )

    def test_weight_curve_male_years(self):
        """
        Test to verify if graphic construct is correct with MALE and YEARS.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )
        self.assertEqual(
            graphic.make(),
            self.male_years
        )
        self.assertEqual(
            graphic.make(WeightCurve.TITLE),
            self.male_years['title']
        )

    def test_weight_curve_female_months(self):
        """
        Test to verify if graphic construct is correct with FEMALE and MONTHS.
        """

        graphic = WeightCurve(
            gender=Constants.FEMALE,
            age=Constants.MONTHS
        )
        self.assertEqual(
            graphic.make(),
            self.female_months
        )
        self.assertEqual(
            graphic.make(WeightCurve.TITLE),
            self.female_months['title']
        )

    def test_weight_curve_female_years(self):
        """
        Test to verify if graphic construct is correct with FEMALE and YEARS.
        """

        graphic = WeightCurve(
            gender=Constants.FEMALE,
            age=Constants.YEARS
        )
        self.assertEqual(
            graphic.make(),
            self.female_years
        )
        self.assertEqual(
            graphic.make(WeightCurve.TITLE),
            self.female_years['title']
        )

    def test_result_months_ok(self):
        """
        Test to check if the result with months is correct.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        # percentis_3
        self.assertEqual(graphic.result(1.88, 0), -1)
        self.assertEqual(graphic.result(1.89, 0), 0)
        self.assertEqual(graphic.result(1.90, 0), 0)
        self.assertEqual(graphic.result(5.58, 10), -1)
        self.assertEqual(graphic.result(5.59, 10), 0)
        self.assertEqual(graphic.result(5.60, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(4.18, 0), 0)
        self.assertEqual(graphic.result(4.19, 0), 0)
        self.assertEqual(graphic.result(4.20, 0), 1)
        self.assertEqual(graphic.result(10.89, 10), 0)
        self.assertEqual(graphic.result(10.90, 10), 0)
        self.assertEqual(graphic.result(10.91, 10), 1)

    def test_result_years_ok(self):
        """
        Test to check if the result with years is correct.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        # percentis_3
        self.assertEqual(graphic.result(9.43, 3), -1)
        self.assertEqual(graphic.result(9.44, 3), 0)
        self.assertEqual(graphic.result(9.45, 3), 0)
        self.assertEqual(graphic.result(19.06, 10), -1)
        self.assertEqual(graphic.result(19.07, 10), 0)
        self.assertEqual(graphic.result(19.08, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(18.21, 3), 0)
        self.assertEqual(graphic.result(18.22, 3), 0)
        self.assertEqual(graphic.result(18.23, 3), 1)
        self.assertEqual(graphic.result(52.83, 10), 0)
        self.assertEqual(graphic.result(52.84, 10), 0)
        self.assertEqual(graphic.result(52.85, 10), 1)

    def test_result_months_invalid(self):
        """
        Test to check if the result with months is incorrect because age is
        incorrect.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        # percentis_3
        self.assertEqual(graphic.result(1.89, 0), 0)
        self.assertEqual(graphic.result(1.89, -1), "Invalid age")
        self.assertEqual(graphic.result(9.88, 36), 0)
        self.assertEqual(graphic.result(9.88, 37), "Invalid age")

    def test_result_years_invalid(self):
        """
        Test to check if the result with years is incorrect because age is
        incorrect.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        # percentis_3
        self.assertEqual(graphic.result(9.44, -5), "Invalid age")
        self.assertEqual(graphic.result(9.44, -1), "Invalid age")
        self.assertEqual(graphic.result(9.44, 0), "Invalid age")
        self.assertEqual(graphic.result(9.44, 1), "Invalid age")
        self.assertEqual(graphic.result(9.44, 2), "Invalid age")
        self.assertEqual(graphic.result(9.44, 3), 0)
        self.assertEqual(graphic.result(40.96, 20), 0)
        self.assertEqual(graphic.result(40.96, 21), "Invalid age")
