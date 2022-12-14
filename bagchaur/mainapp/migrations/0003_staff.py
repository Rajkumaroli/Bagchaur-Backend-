# Generated by Django 4.1.3 on 2022-12-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_janpratinidhi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='', upload_to='images')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('worda', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
