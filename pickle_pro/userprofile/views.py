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
    if request.user.is_authenticated:
        cart_count = cart_count = CartItem.objects.filter(cart__user=request.user).count()
    context = {
        'mango_products': mango_products, 
        'lemon_products': lemon_products,
        'mixed_products': mixed_products, 
        'panjabi_products': panjabi_products, 
        'kerda_products': kerda_products, 
        'carrot_products': carrot_products,
        'cart_count': cart_count,
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

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest

def add_to_cart(request, product_type, product_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method")

    size = request.POST.get('size')
    if size not in ['250g', '500g', '1kg']:
        return HttpResponseBadRequest("Invalid size")

    # Normalize product type to lowercase
    product_type = product_type.lower()

    product_model_map = {
        'mango': MangoProduct,
        'lemon': LemonProduct,
        'mixed': MixedProduct,
        'kerda': KerdaProduct,
        'panjabi': PanjabiProduct,
        'carrot': CarrotProduct
    }

    product_model = product_model_map.get(product_type)
    if not product_model:
        return HttpResponseBadRequest("Invalid product type")

    product = get_object_or_404(product_model, id=product_id)

    price = getattr(product, f'price_{size}', None)
    if price is None:
        return HttpResponseBadRequest("Price not found for selected size")

    cart, _ = Cart.objects.get_or_create(user=request.user)

    content_type = ContentType.objects.get_for_model(product)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
        size=size,
        defaults={'price': price, 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} ({size}) added to your cart!")
    return redirect('cart')



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

from django.http import JsonResponse

def get_cart_items(request, product):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('content_type')  # Optional but good for performance

    cart_items_data = []
    total_price = 0
    product_model = {
        'mango': MangoProduct,
        'lemon': LemonProduct,
        'mixed': MixedProduct,
        'kerda': KerdaProduct,
        'panjabi': PanjabiProduct,
        'carrot': CarrotProduct,
    }.get(product)

    for item in items:
        product = item.product  # ✅ This is the correct way to access the actual product

        if not product:
            continue  # Skip broken items

        cart_items_data.append({
            'id': item.id,
            'name': product.name,
            'image': product.image.url if product.image else '',
            'price': product.price_250g,
            'quantity': item.quantity,
            'total_price': item.total_price()
        })

        total_price += item.total_price()

    return JsonResponse({
        'cart_items': cart_items_data,
        'total_price': total_price,
        "cart_count": cart.items.count()
    })

# from django.http import JsonResponse
# from .models import Cart
# from django.contrib.contenttypes.models import ContentType

# def get_cart_items(request):
#     cart, _ = Cart.objects.get_or_create(user=request.user)
#     items = cart.items.select_related('content_type')  # Optimized

#     cart_items_data = []
#     total_price = 0

#     for item in items:
#         product = item.product  # Access the actual product via GenericForeignKey

#         if not product:
#             continue  # Skip broken/missing products

#         # Dynamically get all prices safely
#         price_250g = getattr(product, 'price_250g', None)
#         price_500g = getattr(product, 'price_500g', None)
#         price_1kg = getattr(product, 'price_1kg', None)

#         # You can use item.size or item.quantity to choose price, here example assumes size
#         # Let's assume item has `size` field: "250g", "500g", "1kg"
#         if hasattr(item, 'size'):
#             if item.size == '250g':
#                 price = price_250g
#             elif item.size == '500g':
#                 price = price_500g
#             elif item.size == '1kg':
#                 price = price_1kg
#             else:
#                 price = price_250g  # default fallback
#         else:
#             price = price_250g  # default if no size field exists

#         # Ensure price is not None
#         if price is None:
#             continue

#         item_total = price * item.quantity
#         total_price += item_total

#         cart_items_data.append({
#             'id': item.id,
#             'name': getattr(product, 'name', 'Unnamed'),
#             'image': product.image.url if getattr(product, 'image', None) else '',
#             'price': item.price,
#             'quantity': item.quantity,
#             'size': getattr(item, 'size', '250g'),
#             'total_price': item_total
#         })

#     return JsonResponse({
#         'cart_items': cart_items_data,
#         'total_price': total_price
#     })

    
# def view_cart(request):
#     user = request.user
#     cart, created = Cart.objects.get_or_create(user=user)
#     cart_items = cart.items.all()
#     # total_price = sum(item.total_price() for item in cart_items)
#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         # 'total_price': total_price,
#     }
#     return render(request, 'cart.html', context)

def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()

    # Correct usage of method
    total_price = sum(item.total_price() for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)
