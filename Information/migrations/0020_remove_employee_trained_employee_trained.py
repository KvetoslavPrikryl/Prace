# Generated by Django 4.0.3 on 2022-06-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0019_remove_employee_trained_employee_trained'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='trained',
        ),
        migrations.AddField(
            model_name='employee',
            name='trained',
            field=models.ManyToManyField(to='Information.trained'),
        ),
    ]
