# Generated by Django 5.0.6 on 2024-07-03 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='greeting_text',
            new_name='greeting',
        ),
    ]
