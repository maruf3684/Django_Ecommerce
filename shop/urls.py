
from django.urls import path
from .views.home import HomeView
from .views.registration import RegistrationView
from .views.productdetail import ProductDetailView
from .views.login import NewLoginView,NewPasswordChangeView
from .views.profile import ProfileView,AddressView
from .views import cart
from .views import checkout
from django.contrib.auth.views import LogoutView,PasswordChangeDoneView
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from django.conf.urls import url


##########################Reset Password part#######################################
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView
from .forms.passwordresetform import MyPasswordResetForm
from .forms.setpasswordform import MySetPasswordForm


urlpatterns = [
    path('',HomeView.as_view(),name='homename'),
    path('<int:id>/',HomeView.as_view(),name='hometwoname'),
    path('product-detail/<int:pk>/',ProductDetailView.as_view(),name='productdetailname'),
    path('signup/',RegistrationView.as_view(),name='registrationname'),
    path('accounts/login/',NewLoginView.as_view(),name='loginname'),
    path('logout/',LogoutView.as_view(next_page='loginname'),name='logout'),
    path('accounts/passwordchange/',NewPasswordChangeView.as_view(success_url='/accounts/passwordchangedone/'),name='passwordchangename'),
    path('accounts/passwordchangedone/',PasswordChangeDoneView.as_view(template_name='shop/passwordchangedone.html'),name='passwordchangedone'),
    path('accounts/profile/',ProfileView.as_view(),name='profilrname'),
    path('accounts/address/',AddressView.as_view(),name='addressname'),

    ######### 2 ta same page show kore cart/add-to-cart
    path('add-to-cart/',cart.add_to_cart,name='cartname'),
    path('cart/',cart.show_cart,name='cartnametwo'),
    ##################### ajax ######################
    path('pluscart/',cart.plus_cart),
    path('minuscart/',cart.minus_cart),
    path('removecart/',cart.remove_cart),

    ###########################################
    path('checkout/',checkout.checkout, name='checkoutname'),
    path('paymentdone/',checkout.paymentdone, name='paymentdonename'),
    path('orders/',checkout.orders,name='orders'),
    path('search/',home.search,name='search'),


    #################password reset#################
    path('password-reset/',PasswordResetView.as_view(template_name='shop/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'),name='password_reset_complete'),





]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
