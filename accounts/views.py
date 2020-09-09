from django.shortcuts import render,redirect

from django.contrib import admin

from django.contrib.auth import ( 
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.

# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('usernam')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next: 
#             return redirect(next)
#         return redirects('/')

#     context = {
#         'form': form, 
#     }
#     return render(request, 'login.html', context)

# def login(request):
#     return render(request, 'sports/login.html')

# def register(request):
#     return render(request, 'sports/register.html')