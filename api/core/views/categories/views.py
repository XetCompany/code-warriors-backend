from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import CategoryRequest

from .serializers import CategoryRequestSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_categories(request):
    categories = CategoryRequest.objects.all()
    serializer = CategoryRequestSerializer(categories, many=True)
    return Response({'data': {"categories": serializer.data}}, status=status.HTTP_200_OK)