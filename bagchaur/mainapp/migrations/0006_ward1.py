# Generated by Django 4.1.3 on 2022-12-31 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_staff_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='', upload_to='images')),
                ('name', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
