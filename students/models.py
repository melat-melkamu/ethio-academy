from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=10, default="Male")
    rank = models.CharField(max_length=20, default="Normal")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name