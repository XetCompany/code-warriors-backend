from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Review, Notification, User
from .serializers import ReviewSerializer, ReviewListSerializer


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Review.objects.filter(host_id=user_id)


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        request.data['sender'] = request.user.id
        notification_id = request.data.get('notification_id')
        if notification_id:
            notification = Notification.objects.get(id=notification_id)
            to_user_id = request.data.get('host')
            to_user = User.objects.get(id=to_user_id)
            notification.is_read = True
            notification.save()

            notification = Notification.objects.create(
                user=to_user,
                message=f'Вы получили отзыв от {request.user.username}',
            )
            to_user.notifications.add(notification)

            notification = Notification.objects.create(
                user=request.user,
                message=f'Вы оставили отзыв для {to_user.username}',
            )
            request.user.notifications.add(notification)

        return super().create(request, *args, **kwargs)


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
