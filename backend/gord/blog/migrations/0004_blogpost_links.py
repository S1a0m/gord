# Generated by Django 5.1.1 on 2024-11-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='links',
            field=models.JSONField(default=list),
        ),
    ]
