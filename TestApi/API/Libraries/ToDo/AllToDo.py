from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ToDo
from ...serializers import ToDoSerializer

class AllToDo(APIView):

    def get(self, request):
        todo = ToDo.objects.filter(host=request.user)
        queryset = ToDoSerializer(todo, many=True)
        return JsonResponse(queryset.data, safe=False)

    def post(self, request):
        queryset = ToDoSerializer(data=request.data)

        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)