from django.http import Http404

from app.models import Request


def get_request_object(pk):
    try:
        request_object = Request.objects.get(pk=pk)
    except Request.DoesNotExist:
        raise Http404("Request not found")
    return request_object