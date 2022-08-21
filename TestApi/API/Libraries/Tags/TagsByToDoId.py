from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import ToDo, Tag
from ...serializers import TagSerializer

class TagByToDoId(APIView):

    def get(self, request, pk_id):
        data = ToDo.objects.get(id=pk_id)

        try:
            if data.host == request.user:
                tag = Tag.objects.filter(notes=data)
                serdata = TagSerializer(tag, many=True)
                return JsonResponse(serdata.data, safe=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)