# Generated by Django 4.1 on 2023-11-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("map", "0009_delete_maprooms"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapRooms",
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
                ("name", models.CharField(max_length=100)),
                ("coordinates_json", models.JSONField()),
            ],
        ),
    ]
