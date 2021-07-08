
from django.shortcuts import render
from django.views import View
from shop.forms.registrationform import UserRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class RegistrationView(View):
    def get(self, request):
        form=UserRegistration()
        return render(request,'shop/registration.html',{'form':form})
    def post(self, request):
        form=UserRegistration(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Registered Succcessfully')
            form.save()
        return render(request,'shop/registration.html',{'form':form})