# Generated by Django 2.0.3 on 2018-07-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('detail', models.TextField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('event_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Page')),
            ],
        ),
    ]
