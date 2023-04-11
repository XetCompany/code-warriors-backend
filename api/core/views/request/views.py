from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.core.views.request.serializers import RequestListOrDetailSerializer, RequestCreateOrUpdateSerializer
from api.core.views.request.utils.request import get_request_object, check_user_is_creator
from app.models import Request, Notification

from rest_framework.permissions import AllowAny, IsAuthenticated


class RequestListOrDetailModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestListOrDetailSerializer
    permission_classes = [AllowAny]


class RequestCreateOrUpdateModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['creator'] = request.user.id
        return super().create(request, *args, **kwargs)


@api_view(['POST'])
def add_response_to_request(request, pk):
    request_object = Request.objects.get(pk=pk)
    request_object.responses.add(request.user)

    creator = request_object.creator

    notification = Notification.objects.create(
        user=creator,
        message=f'{request.user.username} откликнулся на ваш заказ'
    )

    creator.notifications.add(notification)

    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)

@permission_classes((IsAuthenticated,))
@api_view(['DELETE'])
def delete_request_by_pk(request, pk):
    request_object = get_request_object(pk)
    check_user_is_creator(request, request_object)

    request_object.delete()

    return Response({"data": {"message": "deleted success"}}, status=status.HTTP_204_NO_CONTENT)


@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def end_request(request, pk):
    request_object = get_request_object(pk)
    check_user_is_creator(request, request_object)

    request_object.is_active = False
    request_object.save()

    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)
