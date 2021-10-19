from django.http import HttpResponse
from rest_framework import viewsets
from main_app.models import Person
from main_app.serializers import PersonSerializer

def index(request):
    3/0
    return HttpResponse("test page")

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer