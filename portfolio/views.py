from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Portfolio

class PortfolioListView(ListView):
    model=Category
    template_name='Portfolio/index.html'

def PortfolioDetailView(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        portfolio=Portfolio.objects.filter(category=category.id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, 'Portfolio/detail.html', {'category': category, 'portfolio':portfolio})