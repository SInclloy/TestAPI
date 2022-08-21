from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import Tag
from ...serializers import TagSerializer

class TagId(APIView):

    def get(self, request, id):
        tag = Tag.objects.get(id=id)

        try:
            if tag.host == request.user:
                queryset = TagSerializer(tag)
                return JsonResponse(queryset.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)