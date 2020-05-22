# Generated by Django 3.0.6 on 2020-05-10 21:59

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20200508_1259"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Comentsss",
                to="blog.Comment",
            ),
        ),
    ]