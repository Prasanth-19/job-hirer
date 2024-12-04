# Generated by Django 5.1.2 on 2024-10-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_candidate_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='expreience',
            new_name='experience',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='firstname',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='lastname',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='pincode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
