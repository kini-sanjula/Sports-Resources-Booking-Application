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

    firstname=models.CharField(max_length=50)
    lasttname=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=10, choices=gender)
    password=models.CharField(max_length=300)
    branch=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    rollno=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20,choices=type_user)

    class Meta:
        db_table = "user"


    


