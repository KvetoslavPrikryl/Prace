# Generated by Django 4.0.3 on 2022-05-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0006_remove_trained_traineds_trained_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trained',
            name='properties',
        ),
        migrations.AlterField(
            model_name='trained',
            name='name',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
