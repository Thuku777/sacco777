# Generated by Django 3.1 on 2020-10-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20201001_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
