from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from datetime import datetime
import uuid

class MyAccountManager(BaseUserManager):
    # 일반 User 생성 , username = user ID 의미
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError(('아이디는 필수 요소입니다.'))
        if not password:
            raise ValueError(("비밀번호를 입력 해주세요"))
        if not name:
            raise ValueError(('이름은 필수 요소입니다.'))
        
        user = self.model(
            username = username,
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 User 생성
    def create_superuser(self, username, name, password):
        user = self.create_user(
            username = username,
            name = name,
            password = password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Account(AbstractUser, PermissionsMixin):

    username        = models.CharField(max_length=20, verbose_name='아이디', blank=False, null=False , unique=True)
    name            = models.CharField(max_length=20, verbose_name='사용자 이름', null=False, blank=False)
    #password        = models.CharField(max_length=256, verbose_name='비밀번호', null=False, blank=False)
    user_phone      = models.CharField(max_length=20, verbose_name='전화번호', blank=True, null=True)
    create_at       = models.DateTimeField(verbose_name='가입 날짜', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='마지막 로그인', auto_now=True)

    is_active       = models.BooleanField(verbose_name='사용가능 여부', default=True)
    is_admin        = models.BooleanField(verbose_name='어드민 여부', default=False)
    is_staff        = models.BooleanField(verbose_name='스텝여부 여부', default=False)
    is_superuser    = models.BooleanField(verbose_name='슈퍼관리자 여부', default=False)
    
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=100, verbose_name='UUID')
    
    objects = MyAccountManager()
    
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['name'] # 필수로 넣어야 하는 필드 (비밀번호 같은것들은 기본적으로 들어감)
    
    def __str__(self):
        return f"{self.username} ({self.name})"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    class Meta:
        db_table = 'Account'
        verbose_name        = "사용자 리스트"
        verbose_name_plural = "사용자 리스트"