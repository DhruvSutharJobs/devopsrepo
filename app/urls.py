from django.urls import path,include
from . import views
from .cviews import TodoDetails,TodoList

urlpatterns = [
    path('todoslist/', views.todolist),
    path('todosdetails/<str:pk>', views.tododetails),
    path('todosadd',views.todoadd),
    path('todosupdate/<str:pk>', views.todoupdate),
    path('todosdelete/<str:pk>', views.tododelete),
]
urlpatterns = [
    path('class-todos/<int:pk>',TodoDetails.as_view()),
    path('class-todos/',TodoList.as_view())
]