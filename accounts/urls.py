from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path("login/",views.login_page,name="login")
]
