from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ToDo
from ...serializers import ToDoSerializer

class AllToDo(APIView):

    def get(self, request):
        allToDo = ToDo.objects.filter(host=request.user)
        serializer_class = ToDoSerializer(allToDo, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)