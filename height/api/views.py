from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from height.models import HeightCurve
from height.curves import Constants
from .serializers import HeightCurveSerializer, HeightCurveResultSerializer


class HeightCurveMaleMonths(generics.RetrieveAPIView):
    """
    Height-based growth curve for males aged 0 to 36 months view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(HeightCurveMaleMonths, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class HeightCurveMaleYears(generics.RetrieveAPIView):
    """
    Height-based growth curve for males aged 3 to 20 years view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = HeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(HeightCurveMaleYears, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts(years=True)

        return context


class HeightCurveFemaleMonths(generics.RetrieveAPIView):
    """
    Height-based growth curve for females aged 0 to 36 months view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.MONTHS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(HeightCurveFemaleMonths, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class HeightCurveFemaleYears(generics.RetrieveAPIView):
    """
    Height-based growth curve for females aged 3 to 20 years view.
    """

    serializer_class = HeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = HeightCurve(
            gender=Constants.FEMALE,
            age=Constants.YEARS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(HeightCurveFemaleYears, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts(years=True)

        return context


class HeightCurveResultView(generics.GenericAPIView):
    """
    Checks whether past data is within the normal growth curve
    """

    serializer_class = HeightCurveResultSerializer

    @classmethod
    def get_curve(cls, gender, interval):
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

        query_result = graphic.result(
            data['height'],
            data['age']
        )

        result = {'result': query_result}

        return result
