from django.http import Http404

from app.models import Request


def get_request_object(pk):
    try:
        request_object = Request.objects.get(pk=pk)
    except Request.DoesNotExist:
        raise Http404("Request not found")
    return request_object


def check_creator(obj):
    if obj.creator:
        creator_id = obj.creator.id
        creator_username = obj.creator.username
    else:
        creator_id = None
        creator_username = None

    return creator_id, creator_username


def check_executor(obj):
    if obj.executor:
        executor_id = obj.executor.id
        executor_username = obj.executor.username
    else:
        executor_id = None
        executor_username = None

    return executor_id, executor_username

