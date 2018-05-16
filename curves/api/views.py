from rest_framework import generics
from curves.models import HeightCurve
from curves.examples import Constants
from .serializers import HeightCurveSerializer


class HeightCurveMaleMonths(generics.RetrieveAPIView):
    """
    Height-based growth curve for males aged 0 to 36 months view.
    """

    serializer_class = HeightCurveSerializer

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
