from itertools import product
from . models import Productpackage, Packageimages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home(request):
    home_data = Productpackage.objects.all()
    context = {"home_data": home_data}
    return render(request, 'mbapp/homepage.html', context)

@login_required(login_url="login")
def package(request, packagename):
    package_data= Productpackage.objects.get(package_category = packagename)
    p_data = Productpackage.objects.all()
    p_images = Packageimages.objects.filter(product=package_data)
    context = {"p_data":p_data,
               "package_data":package_data,
               "p_images":p_images,
        }
    return render(request, 'mbapp/productpage.html', context)


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'mbapp/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'mbapp/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'mbapp/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'mbapp/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'mbapp/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')


def checkcarousel(request):
    car_images = Packageimages.objects.filter(product_id=1)
    return render(request, 'mbapp/check_carousel.html',{'car_images':car_images})
