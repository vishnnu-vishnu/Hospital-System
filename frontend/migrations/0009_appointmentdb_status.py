# Generated by Django 5.0 on 2024-01-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_contactdb_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdb',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=100, null=True),
        ),
    ]