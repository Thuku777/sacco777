# Generated by Django 3.1 on 2020-09-28 10:57

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(max_length=300)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]