from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Pay

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ['orderNumber', 'description', 'amount']
