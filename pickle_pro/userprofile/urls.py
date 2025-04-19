from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('mango/',mango,name='mango'),
    path('Lemon/',Lemon,name='Lemon'),
    path('Mixed/',Mixed,name='Mixed'),
    path('Panjabi/',Panjabi,name='Panjabi'),
    path('kerda/',kerda,name='kerda'),
    path('Carrot/',Carrot,name='Carrot'),
    path('howwe/',howwe,name='howwe'),
    path('makeour/',makeour,name='makeour'),
    path('products/',products,name='products'),
    path('blogs/',blogs,name='blogs'),
    path('Contact/',Contact,name='Contact'),
    path('createaccount/',createaccount,name='createaccount'),
    path('checkout/',checkout,name='checkout'),
    path('password/',password,name='password'),
    path('login',login_view,name='login'),
    path('contact/', contact_view, name='contact'),
    path('logout',logout_view,name='logout'),
    path('cart/', view_cart, name='cart'),
    path('thankyou/', thankyou, name='thankyou'),
    path('add-to-cart/<str:product_type>/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-quantity/<int:item_id>/<int:quantity>/', update_quantity, name='update_quantity'),
    path('password/', password, name='password'),
    path('send_otp/',send_otp, name='send_otp'),
    path('verify_otp/',verify_otp, name='verify_otp'),
    path('reset_password/',reset_password, name='reset_password'),
    path('ordercomplete/',order_complete, name='ordercomplete'),
    path('term/',term_conditions, name='term'),
    path('privacypolicy/',privacypolicy, name='privacypolicy'),
]