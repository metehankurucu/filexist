# Generated by Django 2.1 on 2018-10-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181019_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='lifetime',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Life Time'),
        ),
    ]
