from app.models import CategoryRequest

from rest_framework import serializers


class CategoryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRequest
        fields = '__all__'
