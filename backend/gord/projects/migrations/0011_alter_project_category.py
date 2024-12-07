# Generated by Django 5.1.1 on 2024-12-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('dev', 'Developpement'), ('cyber', 'Cybersécurité'), ('ia', 'Intelligence Artificielle'), ('math', 'Mathématique'), ('elec', 'Électronique')], default='dev', max_length=50),
        ),
    ]
