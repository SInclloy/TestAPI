from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import ToDo, Tag
from ...serializers import TagSerializer

class TagByToDoId(APIView):

    def get(self, request, id):
        todo = ToDo.objects.get(id=id)

        try:
            if todo.host == request.user:
                tag = Tag.objects.filter(notes=todo)
                queryset = TagSerializer(tag, many=True)
                return JsonResponse(queryset.data, safe=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)