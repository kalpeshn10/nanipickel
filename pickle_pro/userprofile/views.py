from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import ipdb
def home(request):
    return render(request,'home.html')

def mango(request):
    return render(request,'mango.html')

def Lemon(request):
    return render(request,'Lemon.html')

def Mixed(request):
    return render(request,'Mixed.html')

def Panjabi(request):
    return render(request,'Panjabi.html')

def kerda(request):
    return render(request,'kerda.html')

def Carrot(request):
    return render(request,'Carrot.html')

def spicy(request):
    return render(request,'spicy.html')

def sweet(request):
    return render(request,'sweet.html')

def howwe(request):
    return render(request,'howwe.html')

def makeour(request):
    return render(request,'makeour.html')

def products(request):
    return render(request,'products.html')

def blogs(request):
    return render(request,'blogs.html')

def Contact(request):
    return render(request,'Contact.html')

def createaccount(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
         
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'This email Already exists')
            return render(request,'createaccount.html')
        
        created = CustomUser.objects.create(full_name=full_name,email=email, phone_number = phone_number)
        created.set_password(password)
        created.save()
        messages.success(request,'Account created Successfully..')
        return redirect("home")  
    return render(request,'createaccount.html')

def password(request):
    return render(request,'password.html')

