from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import ToDo, Tag
from ...serializers import TagSerializer

class TagByToDoId(APIView):
    def __goto404(self):
        print("goto404")
        return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):

        try:todo = ToDo.objects.get(id=id)
        except:
            return self.__goto404()

        if todo.host != request.user:
            return self.__goto404()
        tag = Tag.objects.filter(notes=todo)

        if tag==None:
            return self.__goto404()

        queryset = TagSerializer(tag, many=True)
        return JsonResponse(queryset.data, safe=False)