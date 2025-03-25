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
    path('spicy/',spicy,name='spicy'),
    path('sweet/',sweet,name='sweet'),
    path('howwe/',howwe,name='howwe'),
    path('makeour/',makeour,name='makeour'),
    path('products/',products,name='products'),
    path('blogs/',blogs,name='blogs'),
    path('Contact/',Contact,name='Contact'),
    path('createaccount/',createaccount,name='createaccount'),
    path('checkout/',checkout,name='checkout'),
    path('password/',password,name='password'),
    path('login',login,name='login'),
    path('product_detail/<int:id>', product_detail, name='product_detail'),
    path('contact/', contact_view, name='contact'),
    path('logout',logout,name='logout'),
    # path('product_detail/<int:id>', product_detail, name='product_detail'),
    # path('home/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    # path('home/remove/<int:item>/', remove_from_cart, name='remove_from_cart')

]