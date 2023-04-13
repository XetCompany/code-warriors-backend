from rest_framework import serializers

from api.core.views.user.serializers import UserSerializer
from app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'
