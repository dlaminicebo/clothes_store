from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#create customer profile
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified=models.DateTimeField(User, auto_now=True)
    phone=models.CharField(max_length=20, blank=True)
    address1=models.CharField(max_length=200, blank=True)
    address2=models.CharField(max_length=200, blank=True)
    city=models.CharField(max_length=200, blank=True)
    state=models.CharField(max_length=200, blank=True)
    zipcode=models.CharField(max_length=200, blank=True)
    country=models.CharField(max_length=200, blank=True)
    old_cart=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
#create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

#Automate the profile thing
post_save.connect(create_profile, sender=User)


#categories of products
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= 'categories'

#customers
class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

#All of our products
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1, related_name='products')
    description=models.CharField(max_length=250, default='', blank=True, null=True)
    image=models.ImageField(upload_to='uploads/product/')

    #Add Sale
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

#customer orders
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100, default='', blank=True)
    phone=models.CharField(max_length=20, default='', blank=True)
    date=models.DateField(default=datetime.date.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id}: {self.product.name} for {self.customer.firstname} {self.customer.lastname}'