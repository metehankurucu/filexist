# Generated by Django 2.1 on 2018-10-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Description'),
        ),
    ]