from rest_framework_simplejwt.views import TokenObtainPairView

from api.auth.login.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
