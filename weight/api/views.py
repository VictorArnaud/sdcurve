from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from weight.models import WeightCurve
from core import Constants
from .serializers import WeightCurveSerializer, WeightCurveResultSerializer


class WeightCurveMaleMonths(generics.RetrieveAPIView):
    """
    Weight-based growth curve for males aged 0 to 36 months view.
    """

    serializer_class = WeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.MONTHS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(WeightCurveMaleMonths, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class WeightCurveMaleYears(generics.RetrieveAPIView):
    """
    Weight-based growth curve for males aged 3 to 20 years view.
    """

    serializer_class = WeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = WeightCurve(
            gender=Constants.MALE,
            age=Constants.YEARS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(WeightCurveMaleYears, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts(years=True)

        return context


class WeightCurveFemaleMonths(generics.RetrieveAPIView):
    """
    Weight-based growth curve for females aged 0 to 36 months view.
    """

    serializer_class = WeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = WeightCurve(
            gender=Constants.FEMALE,
            age=Constants.MONTHS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(WeightCurveFemaleMonths, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class WeightCurveFemaleYears(generics.RetrieveAPIView):
    """
    Weight-based growth curve for females aged 3 to 20 years view.
    """

    serializer_class = WeightCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = WeightCurve(
            gender=Constants.FEMALE,
            age=Constants.YEARS
        )

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(WeightCurveFemaleYears, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts(years=True)

        return context


class WeightCurveResultView(generics.GenericAPIView):
    """
    Checks whether past data is within the normal growth curve
    """

    serializer_class = WeightCurveResultSerializer

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

        graphic = WeightCurve(
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
            data['weight'],
            data['age']
        )

        result = {'result': query_result}

        return result
