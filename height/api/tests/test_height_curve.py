from rest_framework.test import APITestCase
from core import Constants
from height.models import HeightCurve
from height.curves import (
    HeightCurveMaleYears, HeightCurveMaleMonths,
    HeightCurveFemaleYears, HeightCurveFemaleMonths
)


class HeightCurveTestCase(APITestCase):
    """
    Unit test of height-based growth curve
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.male_years = HeightCurveMaleYears().make()
        self.male_months = HeightCurveMaleMonths().make()
        self.female_years = HeightCurveFemaleYears().make()
        self.female_months = HeightCurveFemaleMonths().make()

    def test_height_curve_male_months(self):
        """
        Test to verify if graphic construct is correct with MALE and MONTHS.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )
        self.assertEqual(
            graphic.make(),
            self.male_months
        )
        self.assertEqual(
            graphic.make(HeightCurve.TITLE),
            self.male_months['title']
        )

    def test_height_curve_male_years(self):
        """
        Test to verify if graphic construct is correct with MALE and YEARS.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )
        self.assertEqual(
            graphic.make(),
            self.male_years
        )
        self.assertEqual(
            graphic.make(HeightCurve.TITLE),
            self.male_years['title']
        )

    def test_height_curve_female_months(self):
        """
        Test to verify if graphic construct is correct with FEMALE and MONTHS.
        """

        graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.MONTHS
        )
        self.assertEqual(
            graphic.make(),
            self.female_months
        )
        self.assertEqual(
            graphic.make(HeightCurve.TITLE),
            self.female_months['title']
        )

    def test_height_curve_female_years(self):
        """
        Test to verify if graphic construct is correct with FEMALE and YEARS.
        """

        graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.YEARS
        )
        self.assertEqual(
            graphic.make(),
            self.female_years
        )
        self.assertEqual(
            graphic.make(HeightCurve.TITLE),
            self.female_years['title']
        )

    def test_result_months_ok(self):
        """
        Test to check if the result with months is correct.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        # percentis_3
        self.assertEqual(graphic.result(42.90, 0), -1)
        self.assertEqual(graphic.result(42.91, 0), 0)
        self.assertEqual(graphic.result(42.92, 0), 0)
        self.assertEqual(graphic.result(63.74, 10), -1)
        self.assertEqual(graphic.result(63.75, 10), 0)
        self.assertEqual(graphic.result(63.76, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(53.06, 0), 0)
        self.assertEqual(graphic.result(53.07, 0), 0)
        self.assertEqual(graphic.result(53.08, 0), 1)
        self.assertEqual(graphic.result(76.26, 10), 0)
        self.assertEqual(graphic.result(76.27, 10), 0)
        self.assertEqual(graphic.result(76.28, 10), 1)

    def test_result_years_ok(self):
        """
        Test to check if the result with years is correct.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        # percentis_3
        self.assertEqual(graphic.result(83.24, 3), -1)
        self.assertEqual(graphic.result(83.25, 3), 0)
        self.assertEqual(graphic.result(83.26, 3), 0)
        self.assertEqual(graphic.result(118.42, 10), -1)
        self.assertEqual(graphic.result(118.43, 10), 0)
        self.assertEqual(graphic.result(118.44, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(100.50, 3), 0)
        self.assertEqual(graphic.result(100.51, 3), 0)
        self.assertEqual(graphic.result(100.52, 3), 1)
        self.assertEqual(graphic.result(143.42, 10), 0)
        self.assertEqual(graphic.result(143.43, 10), 0)
        self.assertEqual(graphic.result(143.44, 10), 1)

    def test_result_months_invalid(self):
        """
        Test to check if the result with months is incorrect because age is
        incorrect.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        # percentis_3
        self.assertEqual(graphic.result(42.91, 0), 0)
        self.assertEqual(graphic.result(42.91, -1), "Invalid age")
        self.assertEqual(graphic.result(81.85, 36), 0)
        self.assertEqual(graphic.result(81.85, 37), "Invalid age")

    def test_result_years_invalid(self):
        """
        Test to check if the result with years is incorrect because age is
        incorrect.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        # percentis_3
        self.assertEqual(graphic.result(83.25, -5), "Invalid age")
        self.assertEqual(graphic.result(83.25, -1), "Invalid age")
        self.assertEqual(graphic.result(83.25, 0), "Invalid age")
        self.assertEqual(graphic.result(83.25, 1), "Invalid age")
        self.assertEqual(graphic.result(83.25, 2), "Invalid age")
        self.assertEqual(graphic.result(83.25, 3), 0)
        self.assertEqual(graphic.result(143.83, 20), 0)
        self.assertEqual(graphic.result(143.83, 21), "Invalid age")
