# Generated by Django 3.2.7 on 2022-01-02 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Artisan_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='password2',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
