# Generated by Django 5.1.1 on 2024-11-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('dev', 'Developpement'), ('cyber', 'Cybersécurité'), ('ia', 'Intelligence Artificielle'), ('math', 'Mathématique'), ('elec', 'Électronique')], default='prog', max_length=50),
        ),
    ]
