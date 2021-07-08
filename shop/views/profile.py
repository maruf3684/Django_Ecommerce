
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from shop.forms.customerprofileform import CustomerProfileForm
from shop.models.customer_model import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        form=CustomerProfileForm()
        dict={}
        dict['form']=form
        dict['active']='btn-primary'
        return render(request, 'shop/profile.html', dict)


    def post(self, request, *args, **kwargs):
        form =CustomerProfileForm(request.POST)

        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            city = form.cleaned_data['city']
            locality = form.cleaned_data['locality']
            zipcode = form.cleaned_data['zipcode']
            phone_number = form.cleaned_data['phone_number']
            division = form.cleaned_data['division']
            reg=Customer(user=usr,name=name,city=city,locality=locality,zipcode=zipcode,phone_number=phone_number,division=division)
            reg.save()
            messages.success(request,'Address is Added')

            form = CustomerProfileForm()
            dict = {}
            dict['form'] = form
            dict['active'] = 'btn-primary'
            return render(request, 'shop/profile.html', dict)
        elif not form.is_valid():
            messages.warning(request, 'Address is not Correct')
            form = CustomerProfileForm()
            dict = {}
            dict['form'] = form
            dict['active'] = 'btn-primary'
            return render(request, 'shop/profile.html', dict)



@method_decorator(login_required,name='dispatch')
class AddressView(View):
    def get(self, request, *args, **kwargs):
        add=Customer.objects.filter(user=request.user)
        dict={}
        dict['active']='btn-primary'
        dict['add'] = add
        return render(request, 'shop/address.html',dict)

    def post(self, request, *args, **kwargs):

        return HttpResponse('POST request!')

