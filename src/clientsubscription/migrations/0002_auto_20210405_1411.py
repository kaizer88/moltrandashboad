# Generated by Django 3.0.5 on 2021-04-05 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientsubscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='_type',
            new_name='plan',
        ),
    ]
