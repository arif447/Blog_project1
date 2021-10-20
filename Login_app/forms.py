from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Login_app.models import User_profile

class Signup_form(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class Change_form(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class profile_pic_Form(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['profile_pic',]