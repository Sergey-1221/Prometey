# Generated by Django 4.2.6 on 2023-10-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fio',
            field=models.CharField(default='Иванов Иван Иванович', max_length=300),
            preserve_default=False,
        ),
    ]