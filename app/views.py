from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import *


# Create your views here.


def loginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id']=user.id
            return redirect('list')
            # return render(request, "list.html",{'user_id':user.id})
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')
    return render(request, 'login.html')


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            UserProfile(username_id=username, email=email, password=make_password(password)).save()
            messages.success(request, "Registration Done Successfully!")
        else:
            messages.error(request, "Both password not matched!")
        return redirect('register')
    return render(request, 'register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def add(request):
    userdata=UserProfile.objects.all()
    print(userdata.values())

    return render(request,'create.html',{'userdata':userdata})


def savestudent(request):
    if request.method == 'POST':
        username=request.POST.get('id')
        print(username,'iiiiid')

        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')

        try:
            s = Student.objects.get(Name=name, Subject=subject,username_id=username)
            s.Marks += int(marks)
            s.save()
        except Student.DoesNotExist:
            Student(Name=name, Subject=subject, Marks=marks,username_id=username).save()

        messages.success(request, "Student Details are saved")
        return  redirect('list')



    else:
        return render(request, 'create.html')



def studentlist(request):
    userid=request.session['user_id']

    studentlist= Student.objects.filter(username_id=userid).all()
    return render(request, 'list.html', {"data":studentlist})

def delete_student(request,pk):
    result = Student.objects.get(id=pk)
    result.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('list')

def modify_student(request):
    i = request.GET.get("Name")
    result = Student.objects.get(Name=i)
    return render(request, "update.html", {"data": result})

def update_student(request):
    if request.method == "POST":
        std_id = request.POST.get('std_id')
        name = request.POST.get('name')
        sub = request.POST.get('sub')
        marks = request.POST.get('marks')

        std = Student.objects.filter(id=std_id).update(Name = name,Subject = sub,Marks = marks)
        messages.success(request, "Data updated Successfully")
        return redirect('list')
    # i = request.POST.get("u3")
    # n = request.POST.get("u1")
    # s = request.POST.get("u2")
    # sv = Student.objects.get(Name=i,Subject=n,Marks=s).save()
    # return render(request,'update.html',{'data':sv})
    #
    # return redirect('list')


