from django.shortcuts import render,redirect
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth import ( 
    authenticate,
    login,
    logout
)


# import  models, forms here
from .forms import UserLoginForm, UserRegisterForm




# Create your views here.
def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            user = form.cleaned_data
            login(request, user)
            return redirect('/')
    context = {
        'form': form, 
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    pass