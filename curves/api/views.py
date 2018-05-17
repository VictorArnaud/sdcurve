from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from curves.models import HeightCurve
from curves.examples import Constants
from .serializers import HeightCurveSerializer, HeightCurveResultSerializer


class HeightCurveMaleMonths(generics.RetrieveAPIView):
    """
    Height-based growth curve for males aged 0 to 36 months view.
    """

    serializer_class = HeightCurveSerializer

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

    def get_object(self):
        """
        Get the specific curve.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        return graphic.make()


class HeightCurveMaleYears(generics.RetrieveAPIView):
    """
    Height-based growth curve for males aged 3 to 20 years view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        return graphic.make()


class HeightCurveFemaleMonths(generics.RetrieveAPIView):
    """
    Height-based growth curve for females aged 0 to 36 months view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.MONTHS
        )

        return graphic.make()


class HeightCurveFemaleYears(generics.RetrieveAPIView):
    """
    Height-based growth curve for females aged 3 to 20 years view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.YEARS
        )

        return graphic.make()


class HeightCurveResultView(generics.GenericAPIView):
    """
    Checks whether past data is within the normal growth curve
    """

    serializer_class = HeightCurveResultSerializer

    def get_curve(self, gender, interval):
        """
        Get the specific curve from gender and interval.
        """

        curve_gender = Constants.MALE
        curve_interval = Constants.YEARS

        if gender == 'F':
            curve_gender = Constants.FEMALE

        if interval == 'months':
            curve_interval = Constants.MONTHS

        graphic = HeightCurve(
            gender=curve_gender,
            age=curve_interval
        )

        return graphic

    def post(self, request, *args, **kwargs):
        """
        Get the data and return the JSON result
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = self.get_result(serializer.data)
        return Response(result, status=status.HTTP_200_OK)

    def get_result(self, data):
        """
        Get the result of curve query.
        """

        graphic = self.get_curve(
            data['gender'],
            data['interval']
        )

        result = graphic.result(
            data['height'],
            data['age']
        )

        return result
