from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.core.views.request.serializers import RequestListOrDetailSerializer, RequestCreateOrUpdateSerializer, \
    ResponseSerializer
from api.core.views.request.utils.request import get_request_object, check_user_is_creator
from app.models import Request, Notification

from rest_framework.permissions import AllowAny, IsAuthenticated


class RequestListOrDetailModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestListOrDetailSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def get_requests_by_user_id(request, user_id):
    requests = Request.objects.filter(creator_id=user_id)
    serializer = RequestListOrDetailSerializer(requests, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class RequestCreateOrUpdateModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['creator'] = request.user.id
        return super().create(request, *args, **kwargs)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_response_to_request(request, pk):
    request_object = Request.objects.get(pk=pk)
    if request.user in request_object.responses.all():
        return Response({"data": {"message": "Вы уже откликнулись на этот заказ"}}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data
    data['user'] = request.user.id
    response = ResponseSerializer(data=data)
    response.is_valid(raise_exception=True)
    response_object = response.save()

    request_object.responses.add(response_object)

    notification = Notification.objects.create(
        user=request_object.creator,
        message=f'{request.user.username} откликнулся на ваш заказ'
    )
    request_object.creator.notifications.add(notification)

    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_request_by_pk(request, pk):
    request_object = get_request_object(pk)
    check_user_is_creator(request, request_object)

    request_object.delete()

    return Response({"data": {"message": "deleted success"}}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def end_request(request, pk):
    request_object = get_request_object(pk)
    check_user_is_creator(request, request_object)

    request_object.is_active = False
    request_object.save()

    return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)
