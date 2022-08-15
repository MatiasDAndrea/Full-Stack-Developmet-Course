from django.shortcuts import render, HttpResponse, redirect
from login.forms import LoginForm
from django.urls import reverse
from Clientes.models import Cliente


# Create your views here.
class LoginPackage:

    def home(request):
        return render(request,"Login/home.html")

    def login(request):

        login_form = LoginForm
        return render(request,"Login/login.html",{"form":login_form})

    def login_action(request):
        
        login_form = LoginForm
        data = login_form(data=request.POST)
        info = request.POST
        
        print(Cliente.objects.all)
        return redirect(reverse('Login')+"OK")
