# Generated by Django 4.2.5 on 2023-10-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='finish',
            field=models.BooleanField(default=False, verbose_name='finish check'),
        ),
    ]