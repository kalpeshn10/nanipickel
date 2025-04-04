from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(null=True, blank=True,unique=True, max_length=255)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    

class Category(models.Model):
    Category_name = models.CharField(max_length =20)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/assets/images')

class ContactUs(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    subject = models.CharField(max_length=500,null=True,blank=True)
    message = models.TextField(null=True,blank=True)


class MangoProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name
    
class LemonProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name

class MixedProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name
 
class PanjabiProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name
 
class KerdaProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name

class CarrotProduct(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    mangoproduct = models.ForeignKey(MangoProduct, on_delete=models.CASCADE)
    lemonproduct = models.ForeignKey(LemonProduct, on_delete=models.CASCADE)
    mixedproduct = models.ForeignKey(MixedProduct, on_delete=models.CASCADE)
    kerdaproduct = models.ForeignKey(KerdaProduct, on_delete=models.CASCADE)
    panjabiproduct = models.ForeignKey(PanjabiProduct, on_delete=models.CASCADE)
    carrotproduct = models.ForeignKey(CarrotProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.mangoproduct.price