"""Tailweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    #add
    path('add/',views.add,name="add"),
    path('save/',views.savestudent,name="save"),
    path('list/',views.studentlist,name="list"),

    #update
    path('modify_student/',views.modify_student,name="modify_student"),
    path('update_student/',views.update_student,name="update_student"),
    #delete
    path('delete_student/<int:pk>/',views.delete_student,name="delete_student"),
]
