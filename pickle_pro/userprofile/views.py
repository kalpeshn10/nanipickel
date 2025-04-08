from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.contenttypes.models import ContentType
import ipdb

def home(request):
    mango_products = MangoProduct.objects.order_by('-id').first()
    lemon_products = LemonProduct.objects.order_by('-id').first()
    mixed_products = MixedProduct.objects.order_by('-id').first()
    panjabi_products = PanjabiProduct.objects.order_by('-id').first()
    kerda_products = KerdaProduct.objects.order_by('-id').first()
    carrot_products = CarrotProduct.objects.order_by('-id').first()
    context = {
        'mango_products': mango_products, 
        'lemon_products': lemon_products,
        'mixed_products': mixed_products, 
        'panjabi_products': panjabi_products, 
        'kerda_products': kerda_products, 
        'carrot_products': carrot_products,
    }
    return render(request, 'home.html', context)

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
    carrot_products = CarrotProduct.objects.all()
    return render(request,'Carrot.html', {'carrot_products': carrot_products})

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

        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Invalid email or password')
            return render(request, 'home.html')

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')  

def checkout(request):
    return render(request,'checkout.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if not name:
            messages.error(request,'name is requred')
            return render(request,'Contact.html')
        if not email:
            messages.error(request,'Email is requried')
            return render(request,'Contact.html')

        if ContactUs.objects.filter(email = email).exists():
            messages.error(request,'email alredy exists')
            return render(request,'Contact.html')
        
        created = ContactUs.objects.create(name = name, email=email, subject= subject,message=message)
        created.save()
        send_mail(
                subject = 'Thank you for contacting us',
                message = 'Thankyou for reaching out to us. we will get back to you soon.',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
        )

        send_mail(
            subject=subject,
            message= message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently= False
        )

        messages.success(request,'message sent successfully')
        return render(request, 'Contact.html')
    
    messages.success(request,'somthing went wrong')
    return render(request, 'Contact.html')

def add_to_cart(request, product_type, product_id):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'You must be logged in to add items to your cart.')
        return redirect('login')

    product_model = {
        'mango': MangoProduct,
        'lemon': LemonProduct,
        'mixed': MixedProduct,
        'kerda': KerdaProduct,
        'panjabi': PanjabiProduct,
        'carrot': CarrotProduct,
    }.get(product_type)

    if not product_model:
        messages.error(request, 'Invalid product type.')
        return redirect('createaccount')

    product = get_object_or_404(product_model, id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    content_type = ContentType.objects.get_for_model(product)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} has been added to your cart.')
    return redirect('createaccount')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart_user=request.user)
    cart_item.delete()
    return redirect('createaccount')
