from django.shortcuts import render

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

def home_view(request):
    return render(request, "public/home.html")

def about_view(request):
    return render(request, "public/about.html")

def contact_view(request):
    return render(request, "public/contact.html")
