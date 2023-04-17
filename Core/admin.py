from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_id', 'user_phone', 'is_admin', 'is_staff', 'is_superuser', 'uuid']

    search_fields = ('user_name', 'user_id')
admin.site.register(Account,AccountAdmin) 