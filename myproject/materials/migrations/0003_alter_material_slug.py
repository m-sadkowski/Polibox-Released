# Generated by Django 5.0.6 on 2024-07-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_material_body_material_classes_material_labs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
