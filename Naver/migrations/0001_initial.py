# Generated by Django 4.2 on 2023-04-14 09:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Naver_person",
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
                ("title", models.CharField(max_length=100, verbose_name="질문 제목")),
                (
                    "question",
                    models.CharField(max_length=200, null=True, verbose_name="질문"),
                ),
                (
                    "Answer",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="답변"
                    ),
                ),
                (
                    "question_ID",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="질문자 아이디"
                    ),
                ),
                (
                    "answer_ID",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="답변자 아아디"
                    ),
                ),
                (
                    "question_status",
                    models.CharField(
                        choices=[("Y", "Y"), ("N", "N")],
                        default="N",
                        max_length=6,
                        verbose_name="질문 작성 여부",
                    ),
                ),
                (
                    "answer_status",
                    models.CharField(
                        choices=[("Y", "Y"), ("N", "N")],
                        default="N",
                        max_length=6,
                        verbose_name="답변 작성 여부",
                    ),
                ),
                (
                    "adoption_status",
                    models.CharField(
                        choices=[("Y", "Y"), ("N", "N")],
                        default="N",
                        max_length=6,
                        verbose_name="채택 여부",
                    ),
                ),
                (
                    "naver_url",
                    models.URLField(blank=True, null=True, verbose_name="지식인 URL"),
                ),
                (
                    "creat_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="작성일"
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
            options={
                "verbose_name": "네이버 지식인",
                "verbose_name_plural": "네이버 지식인",
                "db_table": "Naver_person",
            },
        ),
    ]
