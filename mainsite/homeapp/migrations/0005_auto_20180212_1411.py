# Generated by Django 2.0.1 on 2018-02-12 21:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_auto_20180212_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf_tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), default=list, null=True, size=8),
        ),
    ]
