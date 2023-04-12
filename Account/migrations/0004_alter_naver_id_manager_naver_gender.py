# Generated by Django 4.2 on 2023-04-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Account", "0003_alter_naver_id_manager_naver_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="naver_id_manager",
            name="naver_gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "남자"), ("female", "여자"), ("other", "상관없음")],
                max_length=6,
                null=True,
                verbose_name="성별",
            ),
        ),
    ]