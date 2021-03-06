# Generated by Django 2.0.3 on 2018-07-04 10:19

import common.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=120)),
                ('about_content', tinymce.models.HTMLField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='AboutSidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar_title', models.CharField(max_length=120)),
                ('sidebar_pic', models.ImageField(default='default.png', upload_to='pic_folder/', validators=[common.validators.validate_image])),
                ('sidebar_content', tinymce.models.HTMLField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dest_url', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('menu', models.CharField(max_length=120)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True)),
                ('order', models.CharField(max_length=120)),
                ('url', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('excerpt', models.CharField(blank=True, max_length=255)),
                ('is_main', models.BooleanField(default=False)),
                ('is_menu', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_footer_link', models.BooleanField(default=False)),
                ('is_title', models.BooleanField(default=True)),
                ('featured_pic', models.ImageField(default='default.png', upload_to='pic_folder/', validators=[common.validators.validate_image])),
                ('featured_icon', models.ImageField(default='default.png', upload_to='pic_folder/', validators=[common.validators.validate_image])),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=None, related_name='children', to='page.Page')),
            ],
        ),
        migrations.CreateModel(
            name='SubServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured_icon', models.ImageField(default='default.png', upload_to='pic_folder/', validators=[common.validators.validate_image])),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('service_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Page')),
            ],
        ),
        migrations.AddField(
            model_name='button',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttons', to='page.Page'),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together={('slug', 'parent')},
        ),
    ]
