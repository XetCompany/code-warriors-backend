from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.core.views.chat.serializers import MessageSerializer
from app.models import Message


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_chats(request):
    messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
    chats = []
    for message in messages:
        if message.sender == request.user:
            chats.append(message.receiver)
        else:
            chats.append(message.sender)
    chats = set(chats)
    chats = [{
        "name": chat.fullname,
        "id": chat.id,
        "username": chat.username,
    } for chat in chats if chat != request.user]
    return Response({"chats": chats}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_messages(request, user_id):
    messages = Message.objects.filter(sender=request.user, receiver_id=user_id) | Message.objects.filter(
        sender_id=user_id, receiver=request.user)
    messages = sorted(messages, key=lambda message: message.created_at)
    messages_serializer = MessageSerializer(messages, many=True)
    return Response({"messages": messages_serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def send_message(request, user_id):
    data = request.data
    data['sender'] = request.user.id
    data['receiver'] = user_id
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(sender=request.user, receiver_id=user_id)
    return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)

