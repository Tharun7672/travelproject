from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register, name="register"),
    path("login",views.loginview, name="login"),
    path("logout",views.logout,name="logout"),
    path("contact",views.contact,name="contact"),
    path("destinations",views.destinations,name="destinations"),
    path("index",views.index,name="index"),
    path("loginview",views.loginview, name="loginview")
]



