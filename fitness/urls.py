"""
URL configuration for fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("indexx/", views.indexx, name='indexx'),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"), 
    path("new_register/", views.new_register, name="new_register"),
    path("choose_user/", views.choose_user, name="choose_user"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("choose_admin/", views.choose_admin, name="choose_admin"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("user_list/", views.user_list, name="user_list"),
    path("user_delete", views.user_delete, name="user_delete"),
    path("user_profile_delete", views.user_profile_delete, name="user_profile_delete"),
    path("user_search", views.user_search, name="user_search"),
    path("user_profile_search", views.user_profile_search, name="user_profile_search"),
    path("user_modify", views.user_modify, name="user_modify"),
    path("user_profile_modify", views.user_profile_modify, name="user_profile_modify"),


    


     
    



]
