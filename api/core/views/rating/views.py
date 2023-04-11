from rest_framework.decorators import api_view
from django.db.models import Avg
from rest_framework.response import Response

from app.models import User


@api_view(['GET'])
def rating_of_users(request):
    users = User.objects.annotate(avg_rating=Avg('host_user__rating')).order_by('-avg_rating')
    data = {'users': []}
    for user in users:
        data['users'].append({
            'username': user.username,
            'avg_rating': user.avg_rating,
        })
    return Response(data)