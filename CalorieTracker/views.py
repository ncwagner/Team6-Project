from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# Create your views here.
def base(request):
    return render(request, 'registration/',
                  {'Calorie Tracker': base})