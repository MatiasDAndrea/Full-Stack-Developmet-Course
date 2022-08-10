from django.shortcuts import render, HttpResponse

# Create your views here.
class LoginPackage:

    def home(request):
        return render(request,"Login/home.html")

    def login(request):
        return render(request,"Login/login.html")

