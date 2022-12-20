from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # Giris kontrol sistemini yapan hazir fonksiyon


urlpatterns = [
    path("login/", obtain_auth_token),

]
