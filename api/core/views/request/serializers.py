from rest_framework import serializers

from app.models import Request

class RequestSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    executor = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = '__all__'

    def get_creator(self, obj):
        return {
            'id': obj.creator.id,
            'username': obj.creator.username,
        }

    def get_executor(self, obj):
        return {
            'id': obj.executor.id,
            'username': obj.executor.username,
        }