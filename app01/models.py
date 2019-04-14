from django.db import models
# Create your models here.
class classes(models.Model):
    caption=models.CharField(max_length=50)
class student(models.Model):
    user=models.CharField(max_length=20)
    cls=models.ForeignKey("classes",on_delete="null")
class teacher(models.Model):
    user = models.CharField(max_length=20)
    cls=models.ManyToManyField("classes")
class Admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)