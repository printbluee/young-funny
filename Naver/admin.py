from django.contrib import admin
from .models import Naver_person

class Naver_personAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'question_ID', 'creat_at', 'adoption_status', 'uuid']
    # uuid / 질문 제목 / 질문자 아이디 / 작성일 / 채택 여부
    search_fields = ('title', 'question', 'question_ID', 'answer_ID' )
admin.site.register(Naver_person,Naver_personAdmin)