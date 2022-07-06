from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            nm=fm.cleaned_data['name']
            print(nm)
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pm)
            reg.save()
            fm=StudentRegistration()

    else:
        fm = StudentRegistration()
    student = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'student':student})


def delete_data(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')


def update_data(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


