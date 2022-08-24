
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('homepage/',views.homepage,name= "homepage"),
    path('result1/', views.result1,name= "result1"),
    path('result/', views.result,name= "result"),

   path('',views.home,name= "home"),
   path('login', views.login),
   path('signup' , views.signup),
   path('',views.home,name= "home"),
   path('quiz',views.quiz,name="quiz")
]
