from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    host = models.ForeignKey(User, related_name='hosttodo', on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=255)
    description=models.TextField(blank=True)
    time_created=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.title

class Tag(models.Model):
    host = models.ForeignKey(User, related_name='hosttag', on_delete=models.SET_NULL,null=True)
    notes = models.ForeignKey(ToDo, on_delete=models.SET_NULL, null=True, blank=True, related_name='Notes')

    name=models.CharField(max_length=100,db_index=True)
    time_created = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

    def notes_id(self):
        return self.notes.id
