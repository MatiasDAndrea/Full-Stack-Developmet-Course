from django.shortcuts import render

# Create your views here.

# Create your views here.
class LoginPackage:

    def home(request):
        return render(request,"Login/home.html")

    def login(request):

        return render(request,"Login/login.html")

