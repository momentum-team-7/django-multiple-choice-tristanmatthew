# Generated by Django 3.1.7 on 2021-03-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210307_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='tag',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='language',
            field=models.CharField(blank=True, choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Django', 'Django')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Django', 'Django')], max_length=20, null=True),
        ),
    ]
