from django.contrib import admin
from .models import Naver_id_manager

class Naver_id_managerAdmin(admin.ModelAdmin):
    list_display = ['naver_name', 'naver_id', 'naver_gender', 'naver_real_status', 'naver_login_status', 'naver_last_login']
    search_fields = ('naver_name', 'naver_id', 'naver_gender', 'naver_real_status', 'naver_login_status' )
admin.site.register(Naver_id_manager,Naver_id_managerAdmin)