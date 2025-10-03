from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно! Войдите в систему.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Добро пожаловать {user.username}")
            return redirect('index')
        else:
            messages.error(request, "Неверный логин или пароль")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request,"Вы вышли из системы")
    return redirect('index')