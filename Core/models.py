from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

class MyAccountManager(BaseUserManager):
    def create_user(self, user_id, user_name, password=None):
        """
        주어진 이름, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not user_id:
            raise ValueError(('아이디는 필수 요소입니다.'))
        if not password:
            raise ValueError(("비밀번호를 입력 해주세요"))
        if not user_name:
            raise ValueError(('이름은 필수 요소입니다.'))
        
        user = self.model(
            user_id = user_id,
            user_name = user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_id, user_name, password):
        user = self.create_user(
            user_id = user_id,
            password = password,
            user_name = user_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class Account(AbstractUser):
    user_id         = models.CharField(max_length=20, verbose_name='아이디', blank=False, null=False , unique=True)
    user_name       = models.CharField(max_length=20, verbose_name='이름')
    user_phone      = models.CharField(max_length=20, verbose_name='전화번호', blank=True, null=True)

    is_admin        = models.BooleanField(default=False, verbose_name='어드민 여부')
    is_staff        = models.BooleanField(default=False, verbose_name='스텝여부 여부')
    is_superuser    = models.BooleanField(default=False, verbose_name='슈퍼관리자 여부')
    uuid            = models.UUIDField(default=uuid.uuid4, verbose_name='UUID', max_length=100)

    objects = MyAccountManager()

    USERNAME_FIELD  = 'user_id'
    REQUIRED_FIELDS = ['user_name'] # 필수로 넣어야 하는 필드 (비밀번호 같은것들은 기본적으로 들어감)
    
    class Meta:
        db_table = 'Account'
        verbose_name        = "사용자 리스트"
        verbose_name_plural = "사용자 리스트"