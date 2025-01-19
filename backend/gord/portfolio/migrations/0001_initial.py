# Generated by Django 5.1.1 on 2025-01-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('proof_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=150)),
                ('message', models.TextField()),
                ('avatar', models.ImageField(blank=True, default='default_avatar.webp', null=True, upload_to='avatars/')),
            ],
        ),
    ]
