
from price.admin import admin_site
# Register your models here.

from django.contrib.auth.models import User, Group

admin_site.register(User)