from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#Temel API Görüntüleme
@api_view()
def home(request) :
    return Response({
        "message" : "Hello-. It is homepage in api!"
    })

# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır.
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır.
'''
# -------------------------------------------------------------------


#---------------#---------------#---------------#---------------
#DRF FUNCTION VIEWS
#---------------#---------------#---------------#---------------

from .serializers import StudentSerializer
from .models import Student

@api_view() #Default : ['GET']
def student_list(request) : 
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


#---------------#---------------#---------------#---------------
#DRF FUNCTION POST - CREATE
#---------------#---------------#---------------#---------------

@api_view(['POST'])
def students_create(request) :
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message" : "Created Successfully!"
        },status = status.HTTP_201_CREATED)
    else : 
        return Response({
            "message" : "Data not Validated!"
        })


#---------------#---------------#---------------#---------------
#DRF FUNCTION PUT
# StudentSerializer Tek Kayit Görüntüleme
#---------------#---------------#---------------#---------------

@api_view(['GET'])
def student_detail(request,pk):
    student = Student.object.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

