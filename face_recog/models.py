from django.db import models
#from django.utils import timezone

# Create your models here.


class Student(models.Model):
  name = models.CharField(max_length=100)
  registration_id = models.CharField(max_length=20, unique=True)
  branch = models.CharField(max_length=100)
  face_encodings = models.JSONField()

  def __str__(self):
      return self.name


