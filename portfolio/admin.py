from price.admin import admin_site
from django.contrib.auth.models import User, Group

# Register your models here.
from .models import Category, Portfolio

admin_site.register(Category)

admin_site.register(Portfolio)

