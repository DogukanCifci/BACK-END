from rest_framework.response import Response
from rest_framework.decorators import api_view

#Temel API Görüntüleme
@api_view()
def home(request) :
    return Response({
        "message" : "Hello-. It is homepage in api!"
    })


#---------------#---------------#---------------#---------------

from .serializers import StudentSerializer
from .models import Student

@api_view()
def student_list(request) : 
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)