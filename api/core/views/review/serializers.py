from rest_framework import serializers

from api.core.views.user.serializers import UserSerializer
from app.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    host = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
