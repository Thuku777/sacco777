# Generated by Django 3.1 on 2020-10-01 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20201001_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_heading',
            old_name='service_statement',
            new_name='contact_statement',
        ),
    ]
