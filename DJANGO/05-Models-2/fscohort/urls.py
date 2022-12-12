
from django.urls import path

from django.http import HttpResponse

def fscohort(request) :
    return HttpResponse("FSCOHORT")


urlpatterns = [
    path("", fscohort)
]
