# Generated by Django 4.0.5 on 2022-06-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
