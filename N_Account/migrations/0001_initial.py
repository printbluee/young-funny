# Generated by Django 4.2 on 2023-04-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Naver_id_manager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("naver_id", models.CharField(max_length=20, verbose_name="아이디")),
                (
                    "naver_pw",
                    models.CharField(
                        default=None, max_length=20, null=True, verbose_name="비밀번호"
                    ),
                ),
                ("naver_name", models.CharField(max_length=20, verbose_name="이름")),
                (
                    "naver_gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "남자"), ("female", "여자"), ("other", "상관없음")],
                        max_length=6,
                        null=True,
                        verbose_name="성별",
                    ),
                ),
                (
                    "naver_birth",
                    models.DateField(
                        blank=True, max_length=8, null=True, verbose_name="생년월일"
                    ),
                ),
                (
                    "naver_phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="전화번호"
                    ),
                ),
                (
                    "naver_country",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="국가"
                    ),
                ),
                (
                    "naver_join_ip",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="가입 ip"
                    ),
                ),
                (
                    "naver_real_status",
                    models.CharField(
                        blank=True,
                        choices=[("Y", "Y"), ("N", "N")],
                        max_length=6,
                        null=True,
                        verbose_name="실명여부",
                    ),
                ),
                (
                    "naver_login_status",
                    models.CharField(
                        blank=True,
                        choices=[("Y", "Y"), ("N", "N")],
                        max_length=6,
                        null=True,
                        verbose_name="로그인 가능여부",
                    ),
                ),
                (
                    "naver_last_login",
                    models.DateTimeField(auto_now=True, verbose_name="마지막 로그인"),
                ),
                (
                    "naver_pc_agent",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="PC User Agent",
                    ),
                ),
                (
                    "naver_mobile_agent",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Mobile User Agent",
                    ),
                ),
            ],
            options={
                "verbose_name": "네이버 계정 관리",
                "verbose_name_plural": "네이버 계정 관리",
                "db_table": "naver_id_manager",
            },
        ),
    ]