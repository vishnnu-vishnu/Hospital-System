# Generated by Django 4.2.6 on 2023-11-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_doctordb_dep'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordb',
            name='profile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctordb',
            name='qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]