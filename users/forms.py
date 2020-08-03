from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from . models import Profile

class login_form(forms.Form):
    username = forms.CharField(max_length=100)
    pwd = forms.CharField(max_length=100, widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        #fields = '__all__'
        fields = ['username', 'email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserUpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]
