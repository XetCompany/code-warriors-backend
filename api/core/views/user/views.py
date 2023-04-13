from datetime import datetime

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


def func_sort(user):
    is_buy_update = user.is_buy_update and not user.is_expired_update()
    return user.get_avg_rating() * (2 if is_buy_update else 1)


@api_view(['POST'])
def get_users_by_chosen_categories(request):
    categories = request.data.get('categories', [])
    users = User.objects.filter(chosen_categories__id__in=categories)
    users = sorted(users, key=func_sort, reverse=True)
    users = set(users)
    for user in users:
        user.is_buy_update = user.is_buy_update and not user.is_expired_update()
        user.save()
    serializer = UserDetailSerializer(users, many=True)
    return Response({"users": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserDetailSerializer(user)
    return Response({'data': {"user": serializer.data}}, status=status.HTTP_201_CREATED)
