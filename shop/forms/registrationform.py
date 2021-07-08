from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        # labels={'email':'Lmail'}
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'})
        }
    def clean_email(self):
        email=self.cleaned_data.get('email')
        user_count=User.objects.filter(email=email).count()
        if user_count>=1:
            raise forms.ValidationError("This Email Already Registered")
        return email