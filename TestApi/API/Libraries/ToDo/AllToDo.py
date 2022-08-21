from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ToDo
from ...serializers import ToDoSerializer

class AllToDo(APIView):

    def get(self, request):

        try:todo = ToDo.objects.filter(host=request.user)
        except:todo =None

        if todo!=None:
            queryset = ToDoSerializer(todo, many=True)
            return JsonResponse(queryset.data, safe=False)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        queryset = ToDoSerializer(data=request.data)

        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)