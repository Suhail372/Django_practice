from django.db import models

# Create your models here.
def ToDoList(models.Model):
    name=models.CharField(max_length=200)