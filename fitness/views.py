from django.shortcuts import render , redirect
from .services import FitnessServices
import requests


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, "signin.html")

def register(request):
    return render(request, "signup.html")

# def new_register(request):
#     if request.method == 'POST':
#         user_name=request.POST.get("username")
#         user_mail=request.POST.get("email")
#         user_pass=request.POST.get("password")
#         dob=request.POST.get("dob")
#         age=int(request.POST.get("age"))
#         gender=request.POST.get("gender")
#         city=request.POST.get("city")
#         fs=FitnessServices()
#         result=fs.new_register(user_name, user_mail, user_pass, dob, age, gender, city)
#         if result:
#             return render(request, "Success.html")
#         else:
#             return render(request, "failed.html")

def new_register(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        user_mail = request.POST.get("email")
        user_pass = request.POST.get("password")
        dob = request.POST.get("dob")
        age = int(request.POST.get("age") or 0)
        gender=request.POST.get("gender")
        city = request.POST.get("city")

        fs = FitnessServices()
        result = fs.new_register(user_name, user_mail, user_pass, dob, age, gender, city)
        if result:
            return render(request, "Success.html")
        else:
            return render(request, "failed.html")
    
    # For GET requests, show the signup form
    return render(request, "signup.html")

def choose_user(request):
    if request.method == "POST":
        user_mail = request.POST.get("email")
        user_pass = request.POST.get("password")
        fs = FitnessServices()
        result = fs.authenticate(user_mail, user_pass)
        if result:
            request.session['authenticate']=True
            return render(request, "Success.html")
        else:
            return render(request, "failed.html")
        
       

