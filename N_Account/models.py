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
    naver_pw           = models.CharField(max_length=20, verbose_name='비밀번호', default=None, null=True)
    naver_name         = models.CharField(max_length=20, verbose_name='이름')
    naver_gender       = models.CharField(max_length=6 , verbose_name='성별', choices=gender, blank=True, null=True)
    naver_birth        = models.DateField(max_length=8 , verbose_name='생년월일', blank=True, null=True)
    naver_phone        = models.CharField(max_length=20, verbose_name='전화번호', blank=True, null=True)
    naver_country      = models.CharField(max_length=10, verbose_name='국가', blank=True, null=True)
    
    naver_last_login   = models.DateTimeField(verbose_name='마지막 로그인', auto_now=True) # 마지막 로그인
    naver_real_status  = models.CharField(max_length=6 , verbose_name='실명여부', choices=status, blank=True, null=True)
    naver_login_status = models.CharField(max_length=6 , verbose_name='로그인 가능여부', choices=status, blank=True, null=True)

    naver_join_ip      = models.TextField(verbose_name='가입 ip', blank=True, null=True)
    naver_Cookie       = models.TextField(verbose_name='쿠키값', blank=True, null=True)
    naver_pc_agent     = models.CharField(max_length=500, verbose_name='PC User Agent', blank=True, null=True)
    naver_mobile_agent = models.CharField(max_length=500, verbose_name='Mobile User Agent', blank=True, null=True)

    class Meta:
        db_table            = 'naver_id_manager'
        verbose_name        = '네이버 계정 관리'
        verbose_name_plural = '네이버 계정 관리'