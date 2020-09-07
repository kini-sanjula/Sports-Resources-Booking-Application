from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'sports/home.html')
def login(request):
    return render(request, 'sports/login.html')
def logout(request):
    return render(request, 'sports/logout.html')