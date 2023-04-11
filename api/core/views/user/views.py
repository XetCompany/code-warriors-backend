from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.core.views.user.serializers import UserDetailSerializer, UserUpdateSerializer


@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated,))
def user_info(request):
    if request.method == 'PUT':
        serializer = UserUpdateSerializer(data=request.data, instance=request.user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': {"user": serializer.data}}, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        serializer = UserDetailSerializer(request.user)
        return Response({'data': {"user": serializer.data}}, status=status.HTTP_201_CREATED)
