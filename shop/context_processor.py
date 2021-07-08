from shop.models.ctagory_model import Catagory
from shop.models.cart_model import Cart

##This will Pass Dictionary in all template
def cat(request):
    totalitem=0
    all_catagory = Catagory.objects.all()
    if request.user.is_authenticated:
     totalitem=len(Cart.objects.filter(user=request.user))

    return {'all_catagory':all_catagory,'totalitem':totalitem}

