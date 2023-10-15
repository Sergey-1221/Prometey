# Generated by Django 4.2.6 on 2023-10-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_remove_customuser_department_access_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='experience',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fio',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
