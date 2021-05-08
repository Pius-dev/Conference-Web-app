from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Member,Contact
from django import forms
from django.contrib import messages




def  index(request):
    return render(request, 'UCU_EventApp/index.html')


def register(request):
    if "register" in request.POST:
        member = Member(firstname=request.POST["firstname"],
                lastname= request.POST['lastname'],
                email = request.POST['email'],
                gender = request.POST['gender'],
                phoneNumber = request.POST['phoneNumber'],
                address = request.POST['address'],
                participant = request.POST["participant"],
                topic_to_Present = request.POST["topictopresent"]
                )
        member.save()
       
        return redirect('/') 
    return render(request,'UCU_EventApp/register.html')

def  partner(request):
    return render(request, 'UCU_EventApp/partner.html')

def  schedule(request):
    return render(request, 'UCU_EventApp/schedule.html')

def  committee(request):
    return render(request, 'UCU_EventApp/committee.html')

def  about(request):
    return render(request, 'UCU_EventApp/about.html')

def  contact(request):  
    if "contact" in request.POST:
        cont = Contact(fulltname=request.POST["fullname"],
                phoneNumber = request.POST['phoneNumber'],
                email = request.POST['email'],
                message = request.POST['message']
                )
        cont.save()
        return render(request, "UCU_EventApp/contact.html")
        
    return render(request, 'UCU_EventApp/contact.html')

