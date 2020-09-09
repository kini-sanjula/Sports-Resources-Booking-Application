from django.contrib import admin
from django.urls import path, include
from . import views



from django.contrib.auth import views as auth_views
from django.contrib.auth import ( 
    authenticate,
    get_user_model,
    login,
    logout
)


from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]