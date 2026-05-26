from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .forms import SignupForm

# Create your views here.
"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn
"""

class UserLogin(LoginView):
    template_name = "users/login.html"


class UserSignup(CreateView):
    model = User
    form_class = SignupForm
    template_name = "users/signup.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # called after validating data
        # before saving the records
        user = form.save(commit=False)
        pass_text = form.cleaned_data["password"] # plain text
        user.set_password(pass_text) # hashes the password
        user.save()

        # create profile

        # let the process continue
        return super().form_valid(form)


@require_POST
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
