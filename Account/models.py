from django.db import models

gender = (
    ('male'   , '남자'), # 남자
    ('female' , '여자'), # 여자
    ('other'  , '상관없음')  # 선택안함
)

status = (
    ('Y' , 'Y'), 
    ('N' , 'N'), 
)

class Naver_id_manager(models.Model):
    naver_id           = models.CharField(max_length=20, verbose_name='아이디')
    naver_pw           = models.CharField(max_length=20, default=None, null=True, verbose_name='비밀번호')
    naver_name         = models.CharField(max_length=20, verbose_name='이름')
    naver_gender       = models.CharField(max_length=6, choices=gender, blank=True, null=True, verbose_name='성별')
    naver_birth        = models.DateField(max_length=8, verbose_name='생년월일')
    naver_phone        = models.CharField(max_length=20, blank=True, null=True, verbose_name='전화번호')
    naver_country      = models.CharField(max_length=10, blank=True, null=True, verbose_name='국가')
    naver_join_ip      = models.CharField(max_length=20, blank=True, null=True, verbose_name='가입 ip')
    naver_real_status  = models.CharField(max_length=6, choices=status, blank=True, null=True, verbose_name='실명여부')
    naver_login_status = models.CharField(max_length=6, choices=status, blank=True, null=True, verbose_name='로그인 가능여부')
    naver_last_login   = models.DateTimeField(verbose_name='last login',auto_now=True) # 마지막 로그인
    
    class Meta:
        db_table            = 'naver_id_manager'
        verbose_name        = '네이버 계정'
        verbose_name_plural = '네이버 계정'