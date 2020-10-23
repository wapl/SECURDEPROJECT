from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username= forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required. Put a valid email address.')
    id_number=forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta:
      model=User
      fields = ('username', 'email','id_number', 'password1', 'password2' )
class UserLoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  
    
