from rest_framework import serializers


class HeightCurveSerializer(serializers.Serializer):
    """
    Serializer height curve class.
    """

    title = serializers.CharField(read_only=True)

    ages = serializers.ListField(
        child=serializers.IntegerField(read_only=True)
    )

    percentis_3 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_10 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_25 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_50 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_75 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_90 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )

    percentis_97 = serializers.ListField(
        child=serializers.FloatField(read_only=True)
    )
