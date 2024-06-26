from django.contrib import admin

from .models import Borrow_History, Items, Prof, user

# Register your models here.
admin.site.register(Items)
admin.site.register(Borrow_History)
admin.site.register(user)
admin.site.register(Prof)