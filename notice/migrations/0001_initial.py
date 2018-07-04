# Generated by Django 2.0.3 on 2018-07-04 10:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('order', models.CharField(max_length=120)),
                ('publish', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
