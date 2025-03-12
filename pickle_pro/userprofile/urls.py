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
    # path('forgetpassword/',forgetpassword,name='forgetpassword'),
    
]