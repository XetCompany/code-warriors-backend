from rest_framework.decorators import api_view
from django.db.models import Avg
from rest_framework.response import Response

from api.core.views.rating.serializers import RatingUsersSerializer
from app.models import User


@api_view(['GET'])
def rating_of_users(request):
    users = User.objects.annotate(avg_rating=Avg('host_user__rating')).order_by('-avg_rating')
    serializer = RatingUsersSerializer(users, many=True)
    return Response({'users': serializer.data})