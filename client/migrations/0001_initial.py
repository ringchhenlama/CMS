# Generated by Django 2.0.3 on 2018-07-04 10:20

import common.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('logo', models.ImageField(default='default.png', upload_to='client_img/', validators=[common.validators.validate_image])),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('designation', models.CharField(db_index=True, max_length=255)),
                ('photo', models.ImageField(default='default.png', upload_to='client_photo/', validators=[common.validators.validate_image])),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('order', models.CharField(max_length=120)),
                ('url', models.CharField(default='', max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('is_testimonial', models.BooleanField(default=False)),
                ('client_testimonial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='page.Page')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
