# Generated by Django 4.1 on 2022-08-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jwt",
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
                ("access_token", models.TextField()),
                ("refresh", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
        ),
    ]
