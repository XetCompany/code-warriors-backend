from django.core.mail import EmailMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def send_email(request):
    email = EmailMessage('Hello', 'World', to=['zasecrechenas@mail.ru'])
    email.send()
    return Response({'message': 'Hello'})
