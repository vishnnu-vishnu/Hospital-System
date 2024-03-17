# Generated by Django 4.2.6 on 2023-12-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_remove_doctordb_id_alter_doctordb_doctorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordb',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctordb',
            name='doctorid',
            field=models.IntegerField(unique=True),
        ),
    ]
