from django.urls import path
from .views import LoginView, RegisterView, profile

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]