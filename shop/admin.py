from django.contrib import admin
from.models.customer_model import Customer
from .models.ctagory_model import Catagory
from .models.product_model import Product
from .models.orderplaced_model import OrderPlaced
from .models.cart_model import Cart
from django.contrib.auth.models import User


# Register your models here.


# @admin.register(User)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ['id','username','first_name','last_name','email','password']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','city','locality','zipcode','division','phone_number']
    list_filter = ['name']
    search_fields = ['division']

@admin.register(Catagory)
class CatagoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['admin_photo','id','catagory','title','selling_price','discount_price','discription','brand','product_image']
    list_filter = ['catagory']
    search_fields = ['title']
    readonly_fields = ['admin_photo']  #this admin_photo will show photo in admin panel
    list_per_page = 4

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','catagory','product','quantity','status']
    list_filter = ['customer']
    search_fields = ['product']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
    list_filter = ['user']
    search_fields = ['product']
    

    
    



 