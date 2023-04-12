from django.db import models
import uuid
from django.db.models import URLField

status = (
    ('Y' , 'Y'), 
    ('N'   , 'N'), 
)

class Naver_person(models.Model):
    title           = models.CharField(max_length=100, verbose_name='질문 제목')
    question        = models.CharField(max_length=200, null=True, verbose_name='질문')
    Answer          = models.TextField(max_length=500, null=True, verbose_name='답변')
    question_ID     = models.CharField(max_length=50, null=True, verbose_name='질문자 아이디') 
    answer_ID       = models.CharField(max_length=50, null=True, verbose_name='답변자 아아디') 
    question_status = models.CharField(max_length=6, choices=status, default='N', verbose_name='질문 작성 여부')
    answer_status   = models.CharField(max_length=6, choices=status, default='N', verbose_name='답변 작성 여부')
    adoption_status = models.CharField(max_length=6, choices=status, default='N', verbose_name='채택 여부')
    naver_url       = models.URLField(verbose_name='지식인 URL')
    creat_at        = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    uuid            = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
         return self.title
    
    class Meta:
        db_table            = 'Naver_person'
        verbose_name        = '네이버 지식인'
        verbose_name_plural = '네이버 지식인'