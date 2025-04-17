from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class LemonProduct(models.Model):
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True) 
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return self.name

class MixedProduct(models.Model):
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name
 
class PanjabiProduct(models.Model):
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)  
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
 
class KerdaProduct(models.Model):
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name

class CarrotProduct(models.Model):
    name = models.CharField(max_length=100, default='Unnamed')  
    image = models.ImageField(upload_to='static/assets/images')  
    price_250g = models.PositiveIntegerField() 
    price_500g = models.PositiveIntegerField() 
    price_1kg = models.PositiveIntegerField()  
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items',null=True,blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True,blank=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    product = GenericForeignKey('content_type', 'object_id')

    size = models.CharField(max_length=10,null=True,blank=True)
    price = models.PositiveIntegerField(null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)

    def total_price(self):
        return (self.price or 0) * self.quantity 


# class Checkout(models.Model):
#     PAYMENT_CHOICES = [
#         ('Cash On Delivery', 'Cash On Delivery'),
#         ('PayPal', 'PayPal'),
#     ]
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
#     full_name = models.CharField(max_length=100,null=True,blank=True)
#     email = models.CharField(null=True,blank=True)
#     mobile = models.CharField(max_length=100,null=True,blank=True)
#     address = models.TextField(null=True,blank=True)
#     city = models.CharField(max_length=100,null=True,blank=True)
#     state = models.CharField(max_length=100,null=True,blank=True)
#     zipcode = models.CharField(max_length=100,null=True,blank=True)
#     payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='Cash On Delivery',null=True,blank=True)
#     total = models.DecimalField(max_digits=100, decimal_places=2,null=True,blank=True)
#     product = models.ManyToManyField(Product)
    
class Checkout(models.Model):
    PAYMENT_CHOICES = [
        ('Cash On Delivery', 'Cash On Delivery'),
        ('PayPal', 'PayPal'),
    ]
    full_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    zip_code = models.CharField(max_length=100,null=True,blank=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='Cash On Delivery',null=True,blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2,null=True,blank=True)
    product = models.ManyToManyField(Product)