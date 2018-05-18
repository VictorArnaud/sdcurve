from rest_framework.test import APITestCase
from core import Constants
from perimeter.models import PerimeterCurve
from perimeter.curves import PerimeterCurveMale, PerimeterCurveFemale


class PerimeterCurveTestCase(APITestCase):
    """
    Unit test of cephalic perimeter based growth curve
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.male = PerimeterCurveMale().make()
        self.female = PerimeterCurveFemale().make()

    def test_perimeter_curve_male(self):
        """
        Test to verify if graphic construct is correct with MALE gender
        """

        graphic = PerimeterCurve(gender=Constants.MALE)
        self.assertEqual(
            graphic.make(),
            self.male
        )
        self.assertEqual(
            graphic.make(PerimeterCurve.TITLE),
            self.male['title']
        )

    def test_perimeter_curve_female(self):
        """
        Test to verify if graphic construct is correct with FEMALE gender.
        """

        graphic = PerimeterCurve(gender=Constants.FEMALE)
        self.assertEqual(
            graphic.make(),
            self.female
        )
        self.assertEqual(
            graphic.make(PerimeterCurve.TITLE),
            self.female['title']
        )

    def test_result_ok(self):
        """
        Test to check if the result with age is correct.
        """

        graphic = PerimeterCurve(gender=Constants.MALE)

        # percentis_3
        self.assertEqual(graphic.result(30.12, 0), -1)
        self.assertEqual(graphic.result(30.13, 0), 0)
        self.assertEqual(graphic.result(30.14, 0), 0)
        self.assertEqual(graphic.result(40.63, 10), -1)
        self.assertEqual(graphic.result(40.64, 10), 0)
        self.assertEqual(graphic.result(40.65, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(36.14, 0), 0)
        self.assertEqual(graphic.result(36.15, 0), 0)
        self.assertEqual(graphic.result(36.16, 0), 1)
        self.assertEqual(graphic.result(46.27, 10), 0)
        self.assertEqual(graphic.result(46.28, 10), 0)
        self.assertEqual(graphic.result(46.29, 10), 1)

    def test_result_invalid(self):
        """
        Test to check if the result with age is incorrect.
        """

        graphic = PerimeterCurve(gender=Constants.MALE)

        # percentis_3
        self.assertEqual(graphic.result(30.13, 0), 0)
        self.assertEqual(graphic.result(30.13, -1), "Invalid age")
        self.assertEqual(graphic.result(43.08, 24), 0)
        self.assertEqual(graphic.result(43.08, 25), "Invalid age")
