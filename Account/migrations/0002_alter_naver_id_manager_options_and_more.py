# Generated by Django 4.2 on 2023-04-12 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Account", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="naver_id_manager",
            options={"verbose_name": "네이버 계정", "verbose_name_plural": "네이버 계정"},
        ),
        migrations.AlterModelTable(name="naver_id_manager", table="naver_id_manager",),
    ]
