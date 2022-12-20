from rest_framework.pagination import (
    PageNumberPagination, # Default Pagination Method
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'sayfa'

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'
    max_limit = 20 # default_limit etkilenmez. limit=? parametresi için max değeri ifade eder.

class CustomCursorPagination(CursorPagination):
    page_size = 10
    cursor_query_param = 'imlec'
    ordering = '-id' # Cursor için sıralama (tablo sutunu)
