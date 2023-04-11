from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.core.views.user.serializers import NotificationSerializer


@api_view(['GET'])
def get_user_notifications(request):
    notifications = request.user.notifications.filter(
        is_read=False,
    )
    serializer = NotificationSerializer(notifications, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def read_all_notifications(request):
    notifications = request.user.notifications.all()
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)
