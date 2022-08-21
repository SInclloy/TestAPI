from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Tag, ToDo
from ...serializers import ToDoSerializer

class ToDoByTagId(APIView):

    def get(self, request, id):
        tag = Tag.objects.get(id=id)

        try:
            if tag.host == request.user:
                titleToDo = tag.notes
                todo = ToDo.objects.filter(title=titleToDo)
                queryset = ToDoSerializer(todo, many=True)
                return JsonResponse(queryset.data, safe=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)