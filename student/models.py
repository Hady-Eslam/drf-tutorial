from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
