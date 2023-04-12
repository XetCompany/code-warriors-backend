from rest_framework import serializers

from app.models import User


class RatingUsersSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField()

    class Meta:
        model = User
        fields = ('id', 'username', 'avg_rating')