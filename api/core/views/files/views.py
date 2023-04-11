from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Photo, Video


class BaseFileView(APIView):
    model_class = None
    name_field = None

    def get_file(self, file_id):
        try:
            file = self.model_class.objects.get(id=file_id)
        except self.model_class.DoesNotExist:
            raise Http404("File not found")
        return file

    def create_file(self, file):
        args = {self.name_field: file}
        file = self.model_class.objects.create(**args)
        return file

    def get(self, request, *args, **kwargs):
        file_id = kwargs.get('pk')
        file = self.get_file(file_id)
        url = getattr(file, self.name_field).url
        return Response({"data": {"file": url}})

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        image = self.create_file(file)
        return Response({self.name_field: image.id}, status=201)


class ImageView(BaseFileView):
    model_class = Photo
    name_field = 'photo'


class VideoView(BaseFileView):
    model_class = Video
    name_field = 'video'
