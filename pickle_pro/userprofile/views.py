from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth import logout
import ipdb

def home(request):
    return render(request,'home.html')

def mango(request):
    mango_products = MangoProduct.objects.all()
    return render(request, 'mango.html', {'mango_products': mango_products})

def Lemon(request):
    lemon_products = LemonProduct.objects.all()
    return render(request,'Lemon.html', {'lemon_products': lemon_products})

def Mixed(request):
    mixed_products = MixedProduct.objects.all()
    return render(request,'Mixed.html', {'mixed_products': mixed_products})

def Panjabi(request):
    panjabi_products = PanjabiProduct.objects.all()
    return render(request,'Panjabi.html', {'panjabi_products': panjabi_products})

def kerda(request):
    kerda_products = KerdaProduct.objects.all()
    return render(request,'kerda.html', {'kerda_products': kerda_products})

def Carrot(request):
    mango_products = CarrotProduct.objects.all()
    return render(request,'Carrot.html', {'mango_products': mango_products})

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

def login(request):
    if request.method == 'POST':  
        email = request.POST['email']
        print(email)
        password = request.POST['password']

        if not email:
            messages.error(request, 'Email is required')
            return render(request, 'home.html')
        
        if not password:
            messages.error(request, 'Password is required')
            return render(request, 'home.html')

        user_data = authenticate(email=email, password=password)
        if user_data:
            auth_login(request, user_data)
            messages.success(request, 'Login successful')
            return render(request, 'home.html')

        # Check if email exists, but password is incorrect
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Invalid email or password')
            return render(request, 'home.html')

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')  

def checkout(request):
    return render(request,'checkout.html')

