from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    #Fields = ['username', 'password', 'name', 'user_phone', 'is_admin', 'is_staff', 'is_superuser']
    list_display = ('username', 'name', 'user_phone', 'is_admin', 'is_staff', 'is_superuser', 'create_at', 'last_login')
    search_fields = ('username', 'name')
    readonly_fields = ('create_at','last_login')

admin.site.register(Account,AccountAdmin) 