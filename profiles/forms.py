from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=128, 
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Username',
                                    'class': 'form-control'
                                }),
                                label="")
    password = forms.CharField(max_length=64, 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password',
                                    'name': 'password'
                                }),
                                label="")
    remember_me = forms.BooleanField(required=False, 
                                        label="",
                                        widget=forms.CheckboxInput(attrs={
                                            'class': 'form-check-input',
                                            'id': 'remember-me'
                                        }),
                                        help_text="<label class=\"form-check-label\" for=\"remember-me\">Remember me</label>")

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=128, 
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Username',
                                    'class': 'form-control'
                                }),
                                label="")
    password1 = forms.CharField(max_length=64, 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password2',
                                    'name': 'password2'
                                }),
                                label="")
    password2 = forms.CharField(max_length=64, 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Confirm Password',
                                    'class': 'form-control',
                                    'data-toggle': 'password',
                                    'id': 'password2',
                                    'name': 'password2'
                                }),
                                label="")
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']