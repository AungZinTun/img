from django.contrib import admin

# Register your models here.
from .models import Category, Portfolio

admin.site.register(Category)

admin.site.register(Portfolio)