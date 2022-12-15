from django.urls import path
#from .views import home, student_list,students_create,student_detail,student_update,student_delete,student_list_create,student_detail_update_delete

#-----------------------------------FBV-----------------------------------

#after /api :
'''
urlpatterns = [
  path("", home),
  path("student_list/", student_list),
  path("student_create/", students_create),
  path("student_detail/<int:pk>", student_detail), #student_Detail fonksiyonunda pk diye bir parametre kabul ettik onu burada bu sekilde gönderiyoruz. tipip ve degisken adi neyse o '<tip:degisken_adi>'
  path("student_update/<int:pk>", student_update),
  path("student_delete/<int:pk>", student_delete),

  #concat functions()
  path("student_list_create/", student_list_create),
  path("student_detail_update_delete/<int:pk>",student_detail_update_delete)
]
'''


#-----------------------------------#-----------------------------------
#-----------------------------------CBV-----------------------------------
#-----------------------------------#-----------------------------------
from .views import StudentListCreate,home,StudentDetail,StudentGAV,StudentDetailGAV

urlpatterns = [
    path('', home),
    path('student/', StudentListCreate.as_view()), ##Class base kullandigimizda as_view her türlü kullanilmali
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('studentgav/', StudentGAV.as_view()),
    path('studentdetailgav/<int:pk>/', StudentDetailGAV.as_view())
]
