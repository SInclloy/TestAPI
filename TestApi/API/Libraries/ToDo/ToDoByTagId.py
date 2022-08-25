from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Tag, ToDo
from ...serializers import ToDoSerializer

class ToDoByTagId(APIView):

    def __goto404(self):
        return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):

        try:tag = Tag.objects.get(id=id)
        except:
            return self.__goto404()

        if tag.host != request.user:
            return self.__goto404()
        title = tag.notes

        if title == None:
            return self.__goto404()

        todo = ToDo.objects.filter(title=title)

        queryset = ToDoSerializer(todo, many=True)
        return JsonResponse(queryset.data, safe=False)