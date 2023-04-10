from django.http import Http404
from rest_framework.exceptions import PermissionDenied

from app.models import User


def get_user_object(pk):
    try:
        user_object = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404("User not found")
    return user_object


def check_request_user_is_user(request, user_object_id):
    if request.user_id == user_object_id:
        return None
    raise PermissionDenied("У вас нет доступа к этому дейстивию")