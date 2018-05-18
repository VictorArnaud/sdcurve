from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core import Constants
from weight.models import WeightCurve


class WeightCurveMaleMonthsTestCase(APITestCase):
    """
    Test to show the weight-based growth curve for males aged 0 to 36 months
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.url = reverse('weight:curve-male-months')

    def test_graphic_title(self):
        """
        Test to get graphic title.
        """

        self.compare_attributes(
            self.url,
            'title',
            'title'
        )

    def test_graphic_ages(self):
        """
        Test to get graphic ages.
        """

        self.compare_attributes(
            self.url,
            'ages',
            'ages'
        )

    def test_graphic_percentis_3(self):
        """
        Test to get curve 3%.
        """

        self.compare_attributes(
            self.url,
            'percentis_3',
            'percentis_3'
        )

    def test_graphic_percentis_10(self):
        """
        Test to get curve 10%.
        """

        self.compare_attributes(
            self.url,
            'percentis_10',
            'percentis_10'
        )

    def test_graphic_percentis_25(self):
        """
        Test to get curve 25%.
        """

        self.compare_attributes(
            self.url,
            'percentis_25',
            'percentis_25'
        )

    def test_graphic_percentis_50(self):
        """
        Test to get curve 50%.
        """

        self.compare_attributes(
            self.url,
            'percentis_50',
            'percentis_50'
        )

    def test_graphic_percentis_75(self):
        """
        Test to get curve 75%.
        """

        self.compare_attributes(
            self.url,
            'percentis_75',
            'percentis_75'
        )

    def test_graphic_percentis_90(self):
        """
        Test to get curve 90%.
        """

        self.compare_attributes(
            self.url,
            'percentis_90',
            'percentis_90'
        )

    def test_graphic_percentis_97(self):
        """
        Test to get curve 97%.
        """

        self.compare_attributes(
            self.url,
            'percentis_97',
            'percentis_97'
        )

    def compare_attributes(self, url, attribute01, attribute02):
        """
        Compare the graphic result with request result.
        """

        graphic = self.get_graphic()
        graphic = graphic.make()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[attribute01], graphic[attribute02])

    def test_graphic_attribute(self):
        """
        Test to get graphic to plot.
        """

        graphic = self.get_graphic()
        chart = graphic.make_charts()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['graphic'], chart)

    def test_graphic_result_zero(self):
        """
        Result that says the child is of good weight.
        """

        data = {
            'weight': 1.89,
            'age': 0,
            'gender': 'M',
            'interval': 'months'
        }

        url = reverse('weight:curve-result')
        graphic = self.get_graphic()
        result = graphic.result(1.89, 0)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, response.data['result'])
        self.assertTrue(response.data['result'] == 0)

    def test_graphic_result_positive(self):
        """
        Result that says the child is above average weight
        """

        data = {
            'weight': 4.20,
            'age': 0,
            'gender': 'M',
            'interval': 'months'
        }

        url = reverse('weight:curve-result')
        graphic = self.get_graphic()
        result = graphic.result(4.20, 0)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, response.data['result'])
        self.assertTrue(response.data['result'] > 0)

    def test_graphic_result_negative(self):
        """
        Result that says the child is below average weight
        """

        data = {
            'weight': 1.88,
            'age': 0,
            'gender': 'M',
            'interval': 'months'
        }

        url = reverse('weight:curve-result')
        graphic = self.get_graphic()
        result = graphic.result(1.88, 0)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, response.data['result'])
        self.assertTrue(response.data['result'] < 0)

    def get_graphic(self):
        """
        Get the specific graphic.
        """

        graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        return graphic
