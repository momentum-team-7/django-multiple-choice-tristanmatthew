# Generated by Django 3.1.7 on 2021-03-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210308_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Django', 'Django'), ('Other', 'Other')], default='python', max_length=20),
            preserve_default=False,
        ),
    ]
