# Generated by Django 2.0.3 on 2018-07-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slogan', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('logo', models.ImageField(default='default.png', upload_to='site_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Socialsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('icon', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=120)),
            ],
        ),
    ]