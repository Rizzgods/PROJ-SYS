from django.contrib import admin

from .models import Borrow_History, Items

# Register your models here.
admin.site.register(Items)
admin.site.register(Borrow_History)