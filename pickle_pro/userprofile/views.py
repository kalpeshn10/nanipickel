from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
import ipdb

def home(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        context ={
            'queryset' : queryset,
        }
        return render(request,'home.html', context)
    return render(request,'home.html')

def product_detail(request,id):
    category = Category.objects.get(id = id)
    products = Product.objects.filter(Category=category)
    context ={
        "category" : category,
        "products" : products,
    }

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

def login(request):
    if request.method == 'POST':  # Ensure it only processes POST requests
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
    return render(request,'home.html')

def checkout(request):
    return render(request,'checkout.html')

# def view_cart(request):
#     user = request.user
#     cart = Cart.objects.get(user=user)
#     cart_items = cart.items.all()
#     cart_count = cart_items.count()
    
#     context= {
#         'cart': cart,
#         'cart_items': cart_items,
#         'cart_count': cart_count
#     }
#     return render(request,'cart.html',context)

# def add_to_cart(request, product_id):
#     user = request.user
#     if not user.is_authenticated:
#         messages.error(request, 'You must be logged in to add items to your cart.')
#         return redirect('login')

#     product = Product.objects.get(id=product_id)
#     cart, created = Cart.objects.get_or_create(user= request.user)
#     cart_item, created=CartItem.objects.get_or_create(cart=cart, product=product)

    
#     if not created:
#         cart_item.quantity +=1

#     cart_item.save()
#     return redirect('view_cart')

# def remove_from_cart(request, item_id):
#     cart_item = get_object_or_404( CartItem, id=item_id, cart__user=request.user)
#     cart_item.delete()
#     return redirect('view_cart')