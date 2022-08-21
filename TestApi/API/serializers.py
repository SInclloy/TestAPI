
from rest_framework import serializers
from .models import *

class ToDoSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        return ToDo.objects.create(**validated_data)

    class Meta:
        model = ToDo
        fields = '__all__'

class TagSerializerwithToDo(serializers.ModelSerializer):
    notes = ToDoSerializer(many = False)

    def create(self,validated_data):
        return Tag.objects.create(**validated_data)

    class Meta:
        model = Tag
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        return Tag.objects.create(**validated_data)

    class Meta:
        model = Tag
        fields = '__all__'

