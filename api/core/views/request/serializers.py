from rest_framework import serializers

from api.core.views.request.utils.request import check_executor, check_creator
from api.core.views.user.serializers import UserSerializer
from app.models import Request


class RequestListOrDetailSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    executor = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    photos = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()

    responses = UserSerializer(many=True)

    class Meta:
        model = Request
        fields = '__all__'

    def get_creator(self, obj):
        creator_id, creator_username = check_creator(obj)

        return {
            'id': creator_id,
            'username': creator_username,
        }

    def get_photos(self, obj):
        return obj.photos.values_list('photo', flat=True)

    def get_videos(self, obj):
        return obj.videos.values_list('video', flat=True)

    def get_category(self, obj):
        return obj.category.name

    def get_executor(self, obj):
        executor_id, executor_username = check_executor(obj)

        return {
            'id': executor_id,
            'username': executor_username,
        }


class RequestCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'