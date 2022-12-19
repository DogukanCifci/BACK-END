from django.urls import path, include
from .views import (
    home,
    todo_list_create,
    todo_get_del_upd,
    Todos,
    TodoDetail,
    TodoMVS
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', home),
    # fbv urls
    path('todos/', todo_list_create),
    path('todos/<int:id>/', todo_get_del_upd),
    # cbv urls
    path('todo_cls/', Todos.as_view()),
    path('todo_cls/<int:id>/', TodoDetail.as_view()),
    path('', include(router.urls))
]
