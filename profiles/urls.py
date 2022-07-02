from django.urls import path
from .views import LoginView, RegisterView, profile, accept_friend_request, send_friend_request

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<user_id>', profile, name='profile'),
    path('send_friend_request/<user_id>', send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<request_id>', accept_friend_request, name='accept_friend_request'),
]