from rest_framework import serializers

from app.models import User, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Notification
        fields = ('id', 'user')


class UserDetailSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'phone', 'description', 'notifications')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'phone', 'description', 'notifications')