
from django.contrib import admin
from django.urls import path,include
from BlogApp import views

urlpatterns = [
    path('home/', views.home,name='home'),	
    path('post/<id>', views.post),
    path('category/', views.category),
    path('blocked/', views.blocked),
    path('register/', views.register,name = 'register'),	
    path('login/', views.login),		

]
