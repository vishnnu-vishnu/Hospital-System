# Generated by Django 5.0 on 2023-12-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=100, null=True),
        ),
    ]
