from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

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
        user_name = request.POST['user_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        
        if User.objects.filter(user_name=user_name) or User.objects.filter(email=email):
            messages.error(request,'User Already exists')
            return render(request,'createaccount.html')
        
        created = User.objects.create(user_name=user_name,email=email,phone_number=phone_number)
        created.set_password(password)
        created.save()
        messages.success(request,'Account created Successfully..')
        return render(request,"home.html")  
    return render(request,'createaccount.html')

def password(request):
    return render(request,'password.html')

