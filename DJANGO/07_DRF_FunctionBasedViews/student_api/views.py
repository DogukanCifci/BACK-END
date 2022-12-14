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
        },status = status.HTTP_400_BAD_REQUEST)


#---------------#---------------#---------------#---------------
#DRF FUNCTION PUT
# StudentSerializer Tek Kayit Görüntüleme
#---------------#---------------#---------------#---------------

@api_view(['GET'])
def student_detail(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

#---------------#---------------#---------------#---------------
#DRF FUNCTION PUT
# StudentSerializer Tek Kayit Güncelleme
#---------------#---------------#---------------#---------------
@api_view(['PUT'])
def student_update(request,pk) :
    student = Student.objects.get(id=pk) 
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status" : True,
            "message" : "Updated Successfully!"
        },status = status.HTTP_202_ACCEPTED)
    else : 
        return Response({
            "status" : False,
            "message" : "Data not Validated!"
        },status = status.HTTP_400_BAD_REQUEST)



#---------------#---------------#---------------#---------------
# StudentSerializer Tek Kayit Silme
#---------------#---------------#---------------#---------------
@api_view(['DELETE'])
def student_delete(request,pk) :
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({
        "status": True,
        "message" : "Deleted Successfully",
    }, status = status.HTTP_204_NO_CONTENT)

#---------------#---------------#---------------#---------------
#Benzer Functions Concanate :
#---------------#---------------#---------------#---------------
# Listeleme + Yeni Kayit (pk istemeyenler)
@api_view(['GET','POST'])
def student_list_create(request) : 
    if request.method == 'GET':
        #liSTELEME
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method =='POST' :
        #Yeni Kayit
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message" : "Created Successfully!"
        },status = status.HTTP_201_CREATED)
    else : 
        return Response({
            "message" : "Data not Validated!"
        },status = status.HTTP_400_BAD_REQUEST)


#---------------#---------------#---------------#---------------
# Listeleme + Yeni Kayit (pk isteyenler)
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request,pk) : 
    student = Student.objects.get(id=pk) 
    if request.method == 'GET' :
        #Kayit Görüntüleme
        #student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT' :
        # Kayit Güncelleme
        #student = Student.objects.get(id=pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status" : True,
            "message" : "Updated Successfully!"
        },status = status.HTTP_202_ACCEPTED)
        else : 
            return Response({
            "status" : False,
            "message" : "Data not Validated!"
        },status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        #Kayit Silme 
        #student = Student.objects.get(id=pk) #Her seferinde böyle yazmam gerek yok ilk tanimnladigim fonksiyon icinde yazdim zaten
        student.delete()
        return Response({
        "status": True,
        "message" : "Deleted Successfully",
    }, status = status.HTTP_204_NO_CONTENT)
    