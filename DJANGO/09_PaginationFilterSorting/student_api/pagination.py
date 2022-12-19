from rest_framework.pagination import (
    PageNumberPagination
)


class CustomPageNumberPagination(PageNumberPagination) : 
    page_size = 10 #Her bir sayfada kac adet veri olacagini belirtir.
    page_query_param = "sayfa"  #default olarak gelen linkdeki degisken isimlerini bu sekilde kendi istedigimiz isim atayarak kullanabiliriz.

