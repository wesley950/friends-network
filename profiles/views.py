from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm

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
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'profiles/register.html'

@login_required
def profile(request):
    return render(request, 'profiles/profile.html')
