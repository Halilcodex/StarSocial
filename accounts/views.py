from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy, reverse


# Create your views here.
class SignUp(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('accounts:signup')
    success_message = "Sign up was successful"
