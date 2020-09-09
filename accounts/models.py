from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    type_user = [
        ("admin", "admin"),
        ("student", "student"),
    ]

    gender = [
        ("male", "male"),
        ("female", "female"),
    ]
    branch_choices = [
        ("Computer Science", "Computer Science"),
        ("Informational Technology", "Informational Technology"),
        ("Electronics and Communications", "Electronics and Communications"),
        ("BioTech", "BioTech"),
    ]

    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10, choices=gender)
    password=models.CharField(max_length=300)
    branch=models.CharField(max_length=50, choices=branch_choices)
    contact=models.BigIntegerField(unique=True, null = True)
    user_type=models.CharField(max_length=20,choices=type_user, default = "student")

    class Meta:
        db_table = "user"


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=30)

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length = 30)
    roll_no=models.CharField(max_length=20, unique=True)