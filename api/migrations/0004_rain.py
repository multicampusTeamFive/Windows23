# Generated by Django 4.1.7 on 2023-06-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_odfinedust_rename_finedust_idfinedust"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rain",
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
                ("rain", models.BooleanField(default=False)),
            ],
        ),
    ]
