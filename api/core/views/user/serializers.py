from django.contrib.auth.models import Group
from rest_framework import serializers

from api.core.views.categories.serializers import CategoryRequestSerializer
from app.models import User, Notification, Video, Photo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

    def to_internal_value(self, data):
        return User.objects.get(id=data)


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Notification
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    chosen_categories = CategoryRequestSerializer(many=True)
    photos = PhotoSerializer(many=True)
    videos = VideoSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname',
                  'phone', 'description', 'notifications',
                  'chosen_categories', 'photos', 'videos')

    def update(self, instance, validated_data):
        chosen_categories = validated_data.pop('chosen_categories', [])
        photos = validated_data.pop('photos', [])
        videos = validated_data.pop('videos', [])

        instance.chosen_categories.set(chosen_categories)
        instance.photos.set(photos)
        instance.videos.set(videos)

        return super().update(instance, validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)
    chosen_categories = CategoryRequestSerializer(many=True)
    photos = PhotoSerializer(many=True)
    videos = VideoSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname',
                  'phone', 'description', 'notifications',
                  'groups', 'id', 'chosen_categories', 'photos', 'videos')
        read_only_fields = ('notifications', 'groups', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['groups'] = Group.objects.filter(user=instance).values_list('name', flat=True)
        return representation
