

# Create your views here.

import email
from django.shortcuts import render,redirect
from .models import User
import pickle
from django.http import HttpResponse

import joblib
# Create your views here.
# import joblib

def about(request):
  return render (request,"index.html")
def quiz(request):
    return render(request,"quiz.html")

def login(request):
    to = request.GET.get('to')
    if(request.method=="POST"):
        name = request.POST.get('user-name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name,password=password)


            request.session['id'] = user.id
            request.session['email'] = user.email
            request.session['username'] = user.name

            if to:
                return redirect(to)
            return redirect('/home')

        except:
            return render(request,'login.html',{'name':name,'password':password,'error':'please fill correct id and password', 'to':to if to else ""})
    else:
        return render(request,'login.html', {'to':to if to else ""})



def signup(request):
    to = request.GET.get('to')
    if(request.method=="POST"):
        name = request.POST.get('user-name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if name=="" or password=="" or email=="":
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'Please fill all the details.', 'to':to if to else ""})
        try:
            user = User.objects.get(name=name)
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'User name already exists.', 'to':to if to else ""})
        except:
            pass
        try:
            user = User.objects.get(email=email)
            return render(request,'sign.html',{'name':name,'password':password,'email':email,'error':'Email already exists.', 'to':to if to else ""})
        except:
            pass
        user = User.objects.create(name=name,email=email,password=password)
        user.save()
        return redirect('/user/login?to='+(to if to else ""))
    else:
        return render(request,'sign.html', {'to':to if to else ""})




def home(request):
    return render(request,'home.html')


import joblib
def homepage(request):
    return render(request,'homepage.html')


def result(request):
    print("ok")
    cls=joblib.load("Stream_predictor_model.pkl")
    print("yup")
    lis=[]
    lis.append(request.GET['Maths'])
    lis.append(request.GET['English'])
    lis.append(request.GET['SocialScience'])
    lis.append(request.GET['Hindi'])
    lis.append(request.GET['Science'])
    lis.append(request.GET['Computers(optional)'])
    print(lis)
    ans=cls.predict([lis])

    return render(request,"result.html",{'ans':ans})

# def result(request):
#     cls=joblib.load("Stream_predictor_model.pkl")
#
#     lis=[]
#     lis.append(request.GET['Maths'])
#     lis.append(request.GET['English'])
#     lis.append(request.GET['SocialScience'])
#     lis.append(request.GET['Hindi'])
#     lis.append(request.GET['Science'])
#     lis.append(request.GET['Computers(optional)'])
#     print(lis)
#     ans=cls.predict([lis])
#
#     return render(request,"result.html",{'ans':ans})

def result1(request):
    cls=joblib.load("Student_mark_predictor_model.pkl")
    ans = "ok"
    if request.method == 'GET':
        lis=[]
        lis.append(request.GET['Study_hour'])
        print(lis)
        ans=cls.predict([lis])


    return render(request,"ans.html",{'ans':ans})
