# Generated by Django 4.1.2 on 2022-10-21 09:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Package",
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
                ("package_title", models.CharField(max_length=100)),
                ("package_category", models.CharField(max_length=100)),
                ("package_newprice", models.PositiveIntegerField()),
                ("package_oldprice", models.PositiveIntegerField()),
                (
                    "images",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.ImageField(
                            blank=True, null=True, upload_to="media"
                        ),
                        size=20,
                    ),
                ),
                ("package_description", models.CharField(max_length=1000)),
            ],
        ),
    ]