from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Portfolio

class PortfolioListView(ListView):
    model=Category
    template_name='portfolio/index.html'

def PortfolioDetailView(request, slug):

        category = get_object_or_404(Category, slug=slug)
        portfolio=Portfolio.objects.filter(category=category.id)
        return render(request, 'portfolio/detail.html', {'category': category, 'portfolio':portfolio})