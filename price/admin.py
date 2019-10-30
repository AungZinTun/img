from django.contrib import admin

# Register your models here.
from .models import Category, Price

admin.site.register(Category)

admin.site.register(Price)