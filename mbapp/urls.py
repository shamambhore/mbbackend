from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('shop/package/<str:packagename>', views.package, name="package"),
    path('signup',views.signup, name="signup"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('cc',views.checkcarousel, name="checkcarousel"),
    
]
