# Generated by Django 5.1.1 on 2024-09-13 09:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateField()),
                ("is_done", models.BooleanField(default=False)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Hight", "Hight"),
                            ("Medium", "Medium"),
                            ("Low", "Low"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
