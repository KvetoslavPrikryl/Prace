# Generated by Django 4.0.3 on 2022-05-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0016_remove_trained_trained_trained_trained'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trained',
            name='trained',
        ),
        migrations.AddField(
            model_name='employee',
            name='trained',
            field=models.ManyToManyField(to='Information.trained'),
        ),
    ]
