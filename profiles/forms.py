from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=128, 
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Username',
                                    'class': 'form-control'
                                }))
    password = forms.CharField(max_length=64, 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password',
                                    'name': 'password'
                                }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']