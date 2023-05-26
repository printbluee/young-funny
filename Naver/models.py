from django.db import models
import uuid
from django.db.models import URLField

class Naver_person(models.Model):
    title           = models.CharField(max_length=100, verbose_name='질문 제목', blank=False)
    question        = models.TextField(max_length=200, verbose_name='질문', blank=True, null=True)
    Answer          = models.TextField(max_length=500, verbose_name='답변', blank=True, null=True,)
    question_ID     = models.CharField(max_length=50, verbose_name='질문자 아이디', blank=True, null=True) 
    answer_ID       = models.CharField(max_length=50, verbose_name='답변자 아아디', blank=True, null=True) 
    question_status = models.BooleanField(verbose_name='질문 작성 여부', default=False,  blank=True, null=True)
    answer_status   = models.BooleanField(verbose_name='답변 작성 여부', default=False,  blank=True, null=True)
    adoption_status = models.BooleanField(verbose_name='채택 여부', default=False,  blank=True, null=True)
    naver_url       = models.URLField(verbose_name='지식인 URL', blank=True, null=True)
    creat_at        = models.DateTimeField(verbose_name='작성일', auto_now_add=True, blank=True, null=True)
    uuid            = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
         return self.title
    
    class Meta:
        db_table            = 'Naver_person'
        verbose_name        = '네이버 지식인'
        verbose_name_plural = '네이버 지식인'