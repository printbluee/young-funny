from django.contrib import admin
from .models import Naver_id_manager

class Naver_id_managerAdmin(admin.ModelAdmin):
    list_display = ['naver_name', 'naver_id', 'naver_gender', 'naver_real_status', 'naver_login_status', 'naver_last_login']
    # uuid / 질문 제목 / 질문자 아이디 / 작성일 / 채택 여부
    search_fields = ('naver_name', 'naver_id', 'naver_gender', 'naver_real_status', 'naver_login_status' )
admin.site.register(Naver_id_manager,Naver_id_managerAdmin)