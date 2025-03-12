from django.shortcuts import render


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
    return render(request,'createaccount.html')

