from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)


# ------------------- 1.METHOD (PAGE NUMBER PAGINATION) (LOCAL ICIN)
#Keywordler ----> ....../?page=2   ....../?page=5   -->Her bir page'e belli sayida data sinirir koyuyoruz. Ve sayfa olarak hangi sayfaya gitmek istedigimizi seciyoruz.

# class CustomPageNumberPagination(PageNumberPagination) : 
#     page_size = 10 #Her bir sayfada kac adet veri olacagini belirtir.
#     page_query_param = "sayfa"  #default olarak gelen linkdeki degisken isimlerini bu sekilde kendi istedigimiz isim atayarak kullanabiliriz.


# ------------------- 1.METHOD (LIMIT OFFSET PAGINATION) (LOCAL ICIN)
#Keywordler = ...../?limit=15&offset=30 offset anlami 30.kayittan itibaren limit ise 15tane kayit getir demek.

class CustomLimitOffsetPagination(LimitOffsetPagination) :
    default_limit = 15
    limit_query_param='adet'
    offset_query_param ='baslangic'
    max_limit= 9 # limit 15 olsa bile bana en fazla 9 tane veri getirir. Limiti url'de 40 yapsam bile en fazla 9 olur
