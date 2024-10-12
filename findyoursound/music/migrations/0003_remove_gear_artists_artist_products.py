# Generated by Django 5.1.2 on 2024-10-12 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0002_alter_genre_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gear",
            name="artists",
        ),
        migrations.AddField(
            model_name="artist",
            name="products",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="uses",
                to="music.gear",
            ),
        ),
    ]
