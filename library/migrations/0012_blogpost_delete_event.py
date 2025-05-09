# Generated by Django 4.2.19 on 2025-03-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0011_event_delete_blogpost"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Event",
        ),
    ]
