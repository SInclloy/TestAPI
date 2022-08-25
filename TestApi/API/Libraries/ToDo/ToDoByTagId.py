from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Tag, ToDo
from ...serializers import ToDoSerializer

class ToDoByTagId(APIView):

    def get(self, request, id):

        try:tag = Tag.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if tag.host != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        titleTag = tag.notes

        if not titleTag:
            return Response(status=status.HTTP_404_NOT_FOUND)

        todo = ToDo.objects.filter(title=titleTag)

        queryset = ToDoSerializer(todo, many=True)
        return JsonResponse(queryset.data, safe=False)