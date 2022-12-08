from django.shortcuts import render

from django.http import HttpResponse

def home(request) : 
    return HttpResponse("Hello This is our Homepage...")



def students(request) : 
    return HttpResponse("Merhaba Burasi Student Sayfasi!")