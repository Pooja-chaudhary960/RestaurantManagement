from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Waiter)
admin.site.register(Reception)
