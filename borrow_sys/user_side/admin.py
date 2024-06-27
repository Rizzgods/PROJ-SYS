from django.contrib import admin

from .models import Borrow_History, Items, Prof, Students

# Register your models here.
admin.site.register(Items)
admin.site.register(Borrow_History)
admin.site.register(Students)
admin.site.register(Prof)