from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from perimeter.models import PerimeterCurve
from core import Constants
from .serializers import PerimeterCurveSerializer, PerimeterCurveResultSerializer


class PerimeterCurveMale(generics.RetrieveAPIView):
    """
    Cephalic perimeter based growth curve for males aged 0 to 24 months view.
    """

    serializer_class = PerimeterCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = PerimeterCurve(gender=Constants.MALE)

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(PerimeterCurveMale, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class PerimeterCurveFemale(generics.RetrieveAPIView):
    """
    Cephalic perimeter based growth curve for females aged 0 to 24 months view.
    """

    serializer_class = PerimeterCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = PerimeterCurve(gender=Constants.FEMALE)

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(PerimeterCurveFemale, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class PerimeterCurveResultView(generics.GenericAPIView):
    """
    Checks whether past data is within the normal growth curve
    """

    serializer_class = PerimeterCurveResultSerializer

    @classmethod
    def get_curve(cls, gender='M'):
        """
        Get the specific curve from gender and interval.
        """

        curve_gender = Constants.MALE

        if gender == 'F':
            curve_gender = Constants.FEMALE

        graphic = PerimeterCurve(gender=curve_gender)

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

        graphic = self.get_curve(data['gender'])

        query_result = graphic.result(
            data['perimeter'],
            data['age']
        )

        result = {'result': query_result}

        return result
