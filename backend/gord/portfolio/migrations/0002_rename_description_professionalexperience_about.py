# Generated by Django 5.1.1 on 2025-01-19 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionalexperience',
            old_name='description',
            new_name='about',
        ),
    ]
