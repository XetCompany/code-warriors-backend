from rest_framework import serializers

from api.core.views.request.utils.request import check_executor, check_creator
from app.models import Request, User


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RequestSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    executor = serializers.SerializerMethodField()
    responses = ResponseSerializer(many=True)

    class Meta:
        model = Request
        fields = '__all__'

    def get_creator(self, obj):
        creator_id, creator_username = check_creator(obj)

        return {
            'id': creator_id,
            'username': creator_username,
        }

    def get_executor(self, obj):
        executor_id, executor_username = check_executor(obj)

        return {
            'id': executor_id,
            'username': executor_username,
        }