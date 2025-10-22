from django.shortcuts import render , redirect
from .services import FitnessServices
import requests


def indexx(request):
    return render(request, 'index.html')

def login(request):
    return render(request, "signin.html")

def register(request):
    return render(request, "signup.html")

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
        if result:  # result should contain user info
            request.session['authenticate'] = True
            request.session['user_name'] = result['user_name']
            request.session['user_mail'] = result['user_mail']
            request.session['age'] = result['age']
            request.session['gender'] = result['gender']
            request.session['height'] = result['height']
            request.session['weight'] = result['weight']
            return redirect("dashboard")
        else:
            return render(request, "failed.html")
        

def dashboard(request):
    if not request.session.get("authenticate"):
        return redirect("indexx")
    user_name=request.session.get("user_name")
    user_mail=request.session.get("user_mail")
    age=request.session.get("age")
    gender=request.session.get("gender")
    height=request.session.get("height")
    weight=request.session.get("weight")
        # Check if height and weight exist
    if height and weight:
        bmi = round(weight / ((height / 100) ** 2), 2)
    else:
        bmi = None  # or 0, or "N/A"  
    if bmi<18.5:
        bmi_category='UnderWeight'
    elif bmi<25:
        bmi_category='Normal'
    elif bmi<30:
        bmi_category='OverWeight'
    else:
        bmi_category='obese'
    
    return render(request, 'dashboard.html', {'user_name':user_name, 'user_mail':user_mail, 'age':age, 'gender':gender, 'height':height, 'weight':weight, 'bmi':bmi, 'bmi_category':bmi_category})

# def bmi_calculator(request):
#     if not request.session.get("authenticate"):
#         return redirect("indexx")
#     height=request.session.get("height")
#     weight=request.session.get("weight")
#     if height and weight:
#         bmi = round(weight/((height/100)**2), 2)
#     else:
#         bmi = None 

#     if bmi<18.5:
#         bmi_category='UnderWeight'
#     elif bmi<25:
#         bmi_category='Normal'
#     elif bmi<30:
#         bmi_category='OverWeight'
#     else:
#         bmi_category='obese'

#     return render(request, 'dashboard.html', {'bmi':bmi, 'bmi_category':bmi_category})

def adminlogin(request):
    if request.method=="POST":
        admin_mail=request.POST.get("admin_mail")
        admin_pass=request.POST.get("admin_pass")
        fs = FitnessServices()

        result=fs.admin_authentication(admin_mail, admin_pass)
        if result:
            request.session['admin_authenticate']=True
            request.session['admin_name']=result['admin_name']
            request.session['admin_pass']=result['admin_pass']
            return redirect("admin_dashboard")
        else:
            return render(request, "failed.html")