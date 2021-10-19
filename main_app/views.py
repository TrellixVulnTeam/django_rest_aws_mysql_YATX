from django.http import HttpResponse
from rest_framework import viewsets
from main_app.models import Person
from main_app.serializers import PersonSerializer

import logging
logger = logging.getLogger('pybo')

def index(request):
    logger.info("INFO 레벨로 출력")
    return HttpResponse("test page")

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer