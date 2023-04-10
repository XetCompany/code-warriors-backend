from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings
from rest_framework import exceptions


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        serializers.Serializer.__init__(self, *args, **kwargs)
        self.fields['username'] = serializers.CharField(required=False)
        self.fields['email'] = serializers.EmailField(required=False)
        self.fields['password'] = serializers.CharField(required=True)

    def check_fields(self, attrs):
        if not attrs.get('username') and not attrs.get('email'):
            raise serializers.ValidationError('Username or email is required')
        if all([attrs.get('username'), attrs.get('email')]):
            raise serializers.ValidationError('Username and email are mutually exclusive')
        return attrs

    def get_login_field(self, attrs) -> dict:
        if attrs.get('username'):
            return {'username': attrs['username']}
        return {'email': attrs['email']}

    def validate(self, attrs):
        attrs = self.check_fields(attrs)
        authenticate_kwargs = {
            **self.get_login_field(attrs),
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        data = {}

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
