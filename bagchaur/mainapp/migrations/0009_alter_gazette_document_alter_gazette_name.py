# Generated by Django 4.1.3 on 2023-01-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_gazette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gazette',
            name='document',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='gazette',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]