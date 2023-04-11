from django.contrib.auth.models import Group
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
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'phone', 'description', 'notifications', 'groups', 'id')
        read_only_fields = ('notifications', 'groups', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['groups'] = Group.objects.filter(user=instance).values_list('name', flat=True)
        return representation


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'phone', 'description', 'notifications')