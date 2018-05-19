from rest_framework.test import APITestCase
from core import Constants
from imc.models import IMCCurve
from imc.curves import IMCCurveMale, IMCCurveFemale


class IMCCurveTestCase(APITestCase):
    """
    Unit test of IMC based growth curve
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.male = IMCCurveMale().make()
        self.female = IMCCurveFemale().make()

    def test_imc_curve_male(self):
        """
        Test to verify if graphic construct is correct with MALE gender
        """

        graphic = IMCCurve(gender=Constants.MALE)
        self.assertEqual(
            graphic.make(),
            self.male
        )
        self.assertEqual(
            graphic.make(IMCCurve.TITLE),
            self.male['title']
        )

    def test_imc_curve_female(self):
        """
        Test to verify if graphic construct is correct with FEMALE gender.
        """

        graphic = IMCCurve(gender=Constants.FEMALE)
        self.assertEqual(
            graphic.make(),
            self.female
        )
        self.assertEqual(
            graphic.make(IMCCurve.TITLE),
            self.female['title']
        )

    def test_result_ok(self):
        """
        Test to check if the result with age is correct.
        """

        graphic = IMCCurve(gender=Constants.MALE)

        # percentis_3
        self.assertEqual(graphic.result(13.82, 2), -1)
        self.assertEqual(graphic.result(13.83, 2), 0)
        self.assertEqual(graphic.result(13.84, 2), 0)
        self.assertEqual(graphic.result(15.36, 10), -1)
        self.assertEqual(graphic.result(15.37, 10), 0)
        self.assertEqual(graphic.result(15.38, 10), 0)

        # percentis_97
        self.assertEqual(graphic.result(19.70, 2), 0)
        self.assertEqual(graphic.result(19.71, 2), 0)
        self.assertEqual(graphic.result(19.72, 2), 1)
        self.assertEqual(graphic.result(28.26, 10), 0)
        self.assertEqual(graphic.result(28.27, 10), 0)
        self.assertEqual(graphic.result(28.28, 10), 1)

    def test_result_invalid(self):
        """
        Test to check if the result with age is incorrect.
        """

        graphic = IMCCurve(gender=Constants.MALE)

        # percentis_3
        self.assertEqual(graphic.result(13.83, -2), "Invalid age")
        self.assertEqual(graphic.result(13.83, 0), "Invalid age")
        self.assertEqual(graphic.result(13.83, 1), "Invalid age")
        self.assertEqual(graphic.result(13.83, 2), 0)
        self.assertEqual(graphic.result(19.48, 18), 0)
        self.assertEqual(graphic.result(19.48, 19), "Invalid age")
