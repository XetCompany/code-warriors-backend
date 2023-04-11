from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Review
from .serializers import ReviewSerializer, ReviewListSerializer


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Review.objects.filter(host_id=user_id)


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'