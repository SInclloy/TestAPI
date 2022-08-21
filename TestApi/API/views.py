from rest_framework.views import APIView

from .Libraries.ToDo.Header import *
from .Libraries.Tags.Header import *


class ToDo(APIView):

    All = AllToDo
    Id = ToDoId

    ByTagId = ToDoByTagId

class Tag(APIView):

    All = AllTags
    Id = TagId

    ByToDoId = TagByToDoId