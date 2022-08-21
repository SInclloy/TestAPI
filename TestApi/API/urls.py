from .views import *
from django.urls import path

urlpatterns = [
    path('api/Tags/',                          Tag.All.as_view()),
    path('api/Tags/<int:id>/',              Tag.Id.as_view()),
    path('api/TagsByToDo/<int:id>/',        Tag.ByToDoId.as_view()),

    path('api/ToDo/',                          ToDo.All.as_view()),
    path('api/ToDo/<int:id>/',              ToDo.Id.as_view()),
    path('api/ToDoByTag/<int:id>/',         ToDo.ByTagId.as_view()),
]