# Generated by Django 5.1.2 on 2024-10-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_candidate_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='state',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
