from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ToDo
from ...serializers import ToDoSerializer

class ToDoId(APIView):

    def get(self, request, id):
        todo = ToDo.objects.get(id=id)

        try:
            if todo.host == request.user:
                queryset = ToDoSerializer(todo)
                return JsonResponse(queryset.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)