from django.contrib import admin
from .models import *           # In case we dont need all models to be registered under admin we can import one by one

# Register your models here.

admin.site.register(Post)
admin.site.register(User)