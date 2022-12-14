from django.urls import path
from .views import home, student_list

#after /api :
urlpatterns = [
  path("", home),
  path("student_list/", student_list),
]