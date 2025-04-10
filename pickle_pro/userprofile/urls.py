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
    path('login',login,name='login'),
    path('contact/', contact_view, name='contact'),
    path('logout',logout_view,name='logout'),
    path('cart/', view_cart, name='cart'), 
    path('add-to-cart/<str:product_type>/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]