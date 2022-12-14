from django.urls import path
from .views import home, student_list,students_create,student_detail

#after /api :
urlpatterns = [
  path("", home),
  path("student_list/", student_list),
  path("student_create/", students_create),
  path("student_detail/<int:pk>", student_detail) #student_Detail fonksiyonunda pk diye bir parametre kabul ettik onu burada bu sekilde gönderiyoruz. tipip ve degisken adi neyse o '<tip:degisken_adi>'
]