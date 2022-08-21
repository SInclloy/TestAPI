from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ...models import Tag
from ...serializers import TagSerializer

class AllTags(APIView):

    def get(self, request):
        tags = Tag.objects.filter(host=request.user).values()
        queryset = TagSerializer(tags,many=True)
        return JsonResponse(queryset.data, safe=True)

    def post(self, request):
        queryset = TagSerializer(data=request.data)

        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)