# Generated by Django 5.1.1 on 2025-01-16 22:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('unsubscribe_token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Brouillon'), ('sent', 'Envoyée')], default='draft', max_length=10)),
                ('preview_url', models.URLField(blank=True, null=True)),
                ('subscribers', models.ManyToManyField(to='newsletter.subscriber')),
            ],
        ),
    ]
