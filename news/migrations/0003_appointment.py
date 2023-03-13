# Generated by Django 4.1.6 on 2023-03-13 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_text_news_alter_post_title_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('client_name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]