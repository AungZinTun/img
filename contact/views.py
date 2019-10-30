from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Contact

class ContactListView(ListView):
    model=Contact
    template_name='contact/index.html'