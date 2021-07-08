from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from shop.models.product_model import Product
from shop.models.ctagory_model import Catagory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(View):
    def get(self, request,id=None):
        # catid = kwargs['id']
        if id == None:
            all_prod = Product.get_all_product()
        else:
            all_prod = Product.objects.filter(catagory=id).order_by('-id')

        #pagination part
        paginator = Paginator(all_prod, 12) #show 4 item per page
        page_number = request.GET.get('page') #get page number
        page_obj = paginator.get_page(page_number)

        #dicto part
        dicto = {}
        dicto['all_prod']=page_obj
        return render(request,'shop/home.html',dicto)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')



def search(request):
    # pagination part
    if request.method=='GET':
        kk = request.GET.get('kk')
        if kk:
            all_prod = Product.objects.filter(title=kk)
            paginator = Paginator(all_prod, 12)  # show 4 item per page
            page_number = request.GET.get('page')  # get page number
            page_obj = paginator.get_page(page_number)

            # dicto part
            dicto = {}
            dicto['all_prod'] = page_obj
            return render(request, 'shop/search.html', dicto)
        return redirect('/')


