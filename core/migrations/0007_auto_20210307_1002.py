# Generated by Django 3.1.7 on 2021-03-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_snippet_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'verbose_name_plural': 'snippets'},
        ),
    ]
