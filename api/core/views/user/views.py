from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.core.views.user.serializers import UserDetailSerializer, UserUpdateSerializer
from api.core.views.user.utils.user import get_user_object, check_request_user_is_user
from app.models import User


class UserDetailModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]


@permission_classes((IsAuthenticated,))
@api_view(['PUT'])
def user_info_update(request):
    user_object = get_user_object(request.user.id)
    check_request_user_is_user(request, user_object.id)

    serializer = UserUpdateSerializer(data=request.data, instance=user_object, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': {"user": serializer.data}}, status=status.HTTP_201_CREATED)
    return Response({'data': {"error": serializer.errors}}, status=status.HTTP_201_CREATED)