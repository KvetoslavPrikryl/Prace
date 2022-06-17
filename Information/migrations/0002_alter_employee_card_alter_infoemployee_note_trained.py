# Generated by Django 4.0.3 on 2022-04-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='card',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='infoemployee',
            name='note',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.CreateModel(
            name='Trained',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traineds', models.CharField(max_length=1000, null=True)),
                ('properties', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Information.employee')),
            ],
        ),
    ]