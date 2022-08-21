from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import Tag
from ...serializers import TagSerializer, TagSerializerwithToDo

class AllTags(APIView):

    def get(self, request):
        allTags = Tag.objects.filter(host=request.user)
        serializer_class = TagSerializerwithToDo(allTags, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    def post(self, request):
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)