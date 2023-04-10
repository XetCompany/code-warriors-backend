from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.core.views.request.serializers import RequestSerializer
from api.core.views.request.utils.request import get_request_object
from app.models import Request, Notification


class RequestModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


@api_view(['POST'])
def add_response_to_request(request, pk):
    request_object = get_request_object(pk)
    request_object.responses.add(request.user.id)

    creator_id = request_object.creator
    Notification.objects.create(
        user=creator_id,
        # TODO: Поменять вывод
        message=f'{creator_id.username} откликнулся на ваш заказ'
    )

    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)