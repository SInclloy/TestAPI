from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import ToDo, Tag
from ...serializers import TagSerializer

class TagByToDoId(APIView):

    def get(self, request, id):

        try:todo = ToDo.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if todo.host != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tag = Tag.objects.filter(notes=todo)

        if tag==None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = TagSerializer(tag, many=True)
        return JsonResponse(queryset.data, safe=False)