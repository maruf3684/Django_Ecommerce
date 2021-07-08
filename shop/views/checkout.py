from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from shop.models.product_model import Product
from shop.models.ctagory_model import Catagory
from django.core.paginator import Paginator
from shop.models.cart_model import Cart
from shop.models.customer_model import Customer
from shop.models.orderplaced_model import OrderPlaced

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q
from django.http import JsonResponse

@login_required
def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]

    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
        totalamount=amount+shipping_amount

    return render(request,'shop/checkout.html',{'add':add,'totalamount':totalamount,'cartitems':cart_items})

@login_required
def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)



    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")





@login_required
def orders(request):
    op=OrderPlaced.objects.filter(user=request.user)
    return render(request,'shop/orders.html',{'order_placed':op})