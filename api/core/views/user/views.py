from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.core.views.user.serializers import UserDetailSerializer, UserUpdateSerializer
from app.models import User


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


@api_view(['GET'])
def get_users_by_chosen_categories(request):
    categories = request.data.get('categories', [])
    users = User.objects.filter(chosen_categories__id__in=categories)
    serializer = UserDetailSerializer(users, many=True)
    return Response({"users": serializer.data}, status=status.HTTP_200_OK)