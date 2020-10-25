
from school.grates.models import Student
#from django.http import JsonResponse
from school.grates.serializers import StudentSerializer
from rest_framework import viewsets
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
