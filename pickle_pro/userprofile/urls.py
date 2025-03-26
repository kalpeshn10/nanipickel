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

]