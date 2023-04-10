from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Photo, Video


class BaseFileView(APIView):
    model_class = None

    def get_file(self, file_id):
        try:
            file = self.model_class.objects.get(id=file_id)
        except self.model_class.DoesNotExist:
            raise Http404("File not found")
        return file

    def create_file(self, file):
        file = self.model_class.objects.create(file=file)
        return file

    def get(self, request, *args, **kwargs):
        file_id = kwargs.get('pk')
        file = self.get_file(file_id)
        return Response({"data": {"file": file}})

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        image = self.create_file(file)
        return Response({"data": {"files": image}})


class ImageView(BaseFileView):
    model_class = Photo


class VideoView(BaseFileView):
    model_class = Video
