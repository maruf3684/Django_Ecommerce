from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.models.product_model import Product
from shop.models.cart_model import Cart
from shop.models.ctagory_model import Catagory

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q


class ProductDetailView(View):
    def get(self, request,pk):
        all_prod = Product.objects.get(id=pk)  # get na dela loop chalate hobe

        item_already_in_cart=False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=all_prod.id) & Q(user=request.user)).exists()

        print(all_prod)

        return render(request,'shop/productdetail.html',{"dicto":all_prod , 'item_already_in_cart':item_already_in_cart})
