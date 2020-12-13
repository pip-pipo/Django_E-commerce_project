from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return render(request, "root/templets/root/index.html")


def signup(request):
    if request.method == "POST":
        signupFromData = SignUpFrom(request.POST)
        if signupFromData.is_valid():
            messages.success(request, "Congretulation !! You have become an authore")
            signupFromData.save()
    else:
        signupFromData = SignUpFrom()
    return render(request, "root/templets/root/signup.html", {'signupdata': signupFromData})



def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            logindata = LoginFrom(request,data=request.POST)
            if logindata.is_valid():
                uname = logindata.cleaned_data['username']
                upass = logindata.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"login succesfull")
                    return HttpResponseRedirect('/dashboard/')
        else:
            logindata = LoginFrom()
        return render(request, "root/templets/root/login.html",{'logindata':LoginFrom})
    else:
        return HttpResponseRedirect('/dashboard/')


def dashboard(request):
    return render(request,"root/templets/root/dashboard.html")