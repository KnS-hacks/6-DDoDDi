from django.shortcuts import render,redirect, get_object_or_404
from users import models as usermodel
# Create your views here.

def home(request):
    return render(request, "startPage.html")

def mypage(request):
    user = get_object_or_404(usermodel.User, pk=1)
    return render(request, "mainPage.html", {'user':user})

