# Generated by Django 5.1.1 on 2025-01-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_link_alter_summary_summary_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='link',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='summary',
            name='summary_link',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
