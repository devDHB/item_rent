# Generated by Django 4.1.7 on 2023-02-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="제목")),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="원 으로 적어주세요", verbose_name="가격(일)"
                    ),
                ),
                ("description", models.TextField(verbose_name="설명")),
                (
                    "region",
                    models.CharField(
                        help_text="시, 구 로 적어주세요", max_length=120, verbose_name="지역"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
