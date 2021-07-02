from django.db import models
from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    photo = models.ImageField()


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField()
    salary = models.IntegerField()
    phone_number = models.IntegerField()
    achievements = models.TextField()
    email = models.EmailField()


class PostWorker(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.RESTRICT)
    skill = models.CharField(max_length=50)
    skill_comment = models.TextField()


class Enterprise(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    salary = models.IntegerField()
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()


class PostEnterprise(models.Model):
    Enterprise = models.ForeignKey('Enterprise', on_delete=models.RESTRICT)
    skill = models.CharField(max_length=50)
    skill_comment = models.TextField()

