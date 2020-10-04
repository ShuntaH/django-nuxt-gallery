from rest_framework import serializers
from .models import Photos


class WaterPlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = (
            "id",
            "picture",
            'description',
        )
