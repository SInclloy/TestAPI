from .views import *
from django.urls import path

urlpatterns = [
    path('api/Tags/',                          Tag.All.as_view()),
    path('api/Tags/<int:pk_id>/',              Tag.Id.as_view()),
    path('api/TagsByToDo/<int:pk_id>/',        Tag.ByToDoId.as_view()),

    path('api/ToDo/',                          ToDo.All.as_view()),
    path('api/ToDo/<int:pk_id>/',              ToDo.Id.as_view()),
    path('api/ToDoByTag/<int:pk_id>/',         ToDo.ByTagId.as_view()),
]