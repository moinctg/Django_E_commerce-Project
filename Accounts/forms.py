from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
           model = User
           fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
     first_name = forms.CharField(label='First Name')
     last_name = forms.CharField(label='Last Name')
     class Meta:
        model = User
        fields = ['username','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
   present_address = forms.CharField(label='Present Addres')
   perment_address = forms.CharField(label='perment Addres')
   bio = forms.CharField(label='Bio')
   birthday =forms.DateField()
   contact =forms.CharField(label='contact')
   class Meta:
        model = profile
        fields =['present_address','perment_address','bio','birthday','image','contact']