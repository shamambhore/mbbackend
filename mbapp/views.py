from django.shortcuts import render
from . models import Package, Homeimages, Packageimages



def home(request):
    home_data = Package.objects.all()
    home_images = Homeimages.objects.all()
    context = {"home_data": home_data, "home_images":home_images}
    return render(request, 'mbapp/homepage.html', context)

def package(request):
    return render(request, 'mbapp/productpage.html')