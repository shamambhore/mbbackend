from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('shop/package/<str:packagename>', views.package, name="package")
]
