from django.contrib import admin
from .models import User, Faculty, Students


# Register your models here.
admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Students)