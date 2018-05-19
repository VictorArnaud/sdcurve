from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from imc.models import IMCCurve
from core import Constants
from .serializers import IMCCurveSerializer, IMCCurveResultSerializer


class IMCCurveMale(generics.RetrieveAPIView):
    """
    IMC based growth curve for males aged 2 to 18 years view.
    """

    serializer_class = IMCCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = IMCCurve(gender=Constants.MALE)

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(IMCCurveMale, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class IMCCurveFemale(generics.RetrieveAPIView):
    """
    IMC based growth curve for females aged 2 to 18 years view.
    """

    serializer_class = IMCCurveSerializer

    def get_object(self):
        """
        Get the specific curve.
        """

        self.graphic = IMCCurve(gender=Constants.FEMALE)

        return self.graphic.make()

    def get_serializer_context(self):
        """
        Insert some attribute inside serializer.
        """

        context = super(IMCCurveFemale, self).get_serializer_context()
        context['graphic'] = self.graphic.make_charts()

        return context


class IMCCurveResultView(generics.GenericAPIView):
    """
    Checks whether past data is within the normal growth curve
    """

    serializer_class = IMCCurveResultSerializer

    @classmethod
    def get_curve(cls, gender='M'):
        """
        Get the specific curve from gender and interval.
        """

        curve_gender = Constants.MALE

        if gender == 'F':
            curve_gender = Constants.FEMALE

        graphic = IMCCurve(gender=curve_gender)

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

        imc = data['weight'] / (data['height'] ** 2)

        query_result = graphic.result(
            imc,
            data['age']
        )

        result = {'result': query_result}

        return result
