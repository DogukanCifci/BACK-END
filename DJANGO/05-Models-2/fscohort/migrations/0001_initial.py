# Generated by Django 4.1.4 on 2022-12-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(default="", max_length=50)),
                ("last_name", models.CharField(default="", max_length=50)),
                ("number", models.IntegerField(default=0)),
            ],
            options={"ordering": ["-number"],},
        ),
    ]