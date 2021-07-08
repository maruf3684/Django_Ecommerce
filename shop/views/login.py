
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetConfirmView
from shop.forms.loginform import UserLogin
from shop.forms.passwordchangeform import MyPasswoedChangeForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class NewLoginView(LoginView):
    template_name = 'shop/login.html'
    authentication_form =UserLogin

class NewPasswordChangeView(PasswordChangeView):
    template_name = 'shop/passwordchange.html'
    form_class =MyPasswoedChangeForm

