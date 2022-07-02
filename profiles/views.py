from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from profiles.models import FriendRequest

from .forms import LoginForm, RegistrationForm
from .models import User

class LoginView(BaseLoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'profiles/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        
        return super(LoginView, self).form_valid(form)

class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'profiles/register.html'

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friend_requests = None
    friends = user.friends.all()
    is_friend = False
    if user == request.user:
        friend_requests = FriendRequest.objects.filter(receiver=user)
    else:
        is_friend = request.user in friends
    return render(request, 'profiles/profile.html', { 'target_profile': user, 'friend_requests': friend_requests, 'is_friend': is_friend, 'friends': friends })

@login_required
def send_friend_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    friend_request, created = FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
    if created:
        return HttpResponseRedirect(reverse('profiles:profile', args=(receiver.id, )))
    else:
        return HttpResponseRedirect(reverse('profiles:profile', args=(request.user.id, )))

@login_required
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.receiver == request.user:
        friend_request.receiver.friends.add(friend_request.sender)
        friend_request.sender.friends.add(friend_request.receiver)
        friend_request.delete()
    return HttpResponseRedirect(reverse('profiles:profile', args=(friend_request.sender.id, )))
