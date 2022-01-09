
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product



class UserRegisterForm(UserCreationForm):
   
   class Meta:
      model = User
      fields = ['first_name', 'username', 'email', 'password1', 'password2']


class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku','name','quantity','price']
        