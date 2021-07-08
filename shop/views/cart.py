from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from shop.models.product_model import Product
from shop.models.ctagory_model import Catagory
from django.core.paginator import Paginator
from shop.models.cart_model import Cart

from django.db.models import Q
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    cart=Cart(user=user,product=product)
    cart.save()
    return redirect('/cart')

@login_required()
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)

        amount=0.0
        shipping_amount=70.0
        totalamount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]

        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discount_price)
                amount+=tempamount
                totalamount=amount+shipping_amount
            return render(request,'shop/cart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request, 'shop/empty.html')




def plus_cart(request):
    if request.method=="GET":
        user = request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)&Q(user=request.user))
        c.quantity+=1
        c.save()

        amount=0.0
        shipping_amount=70.0
        totalamount = 0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount


        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount+ shipping_amount
        }
        return JsonResponse(data)





def minus_cart(request):
    if request.method=="GET":
        user = request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)&Q(user=request.user))
        c.quantity-=1
        c.save()

        amount=0.0
        shipping_amount=70.0
        totalamount = 0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount


        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount+ shipping_amount
        }
        return JsonResponse(data)



def remove_cart(request):
    if request.method=="GET":
        user = request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)&Q(user=request.user))
        c.delete()

        amount=0.0
        shipping_amount=70.0
        totalamount = 0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount


        data={
            'amount':amount,
            'totalamount':totalamount+ shipping_amount
        }
        return JsonResponse(data)
