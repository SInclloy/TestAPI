from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import ToDo
from ...serializers import ToDoSerializer

class ToDoId(APIView):

    def get(self, request, pk_id):
        data = ToDo.objects.get(id=pk_id)

        try:
            if data.host == request.user:
                serdata = ToDoSerializer(data)
                return JsonResponse(serdata.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)