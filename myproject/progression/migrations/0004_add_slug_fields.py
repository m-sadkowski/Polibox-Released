# progression/migrations/0004_add_slug_fields.py
from django.db import migrations, models
from django.utils.text import slugify
import itertools

def generate_unique_slug(instance, model, name_field):
    base_slug = slugify(getattr(instance, name_field))
    slug = base_slug
    for i in itertools.count(1):
        if not model.objects.filter(slug=slug).exists():
            break
        slug = f'{base_slug}-{i}'
    return slug

def set_unique_slugs(apps, schema_editor):
    Direction = apps.get_model('progression', 'Direction')
    Subject = apps.get_model('progression', 'Subject')

    for direction in Direction.objects.all():
        direction.slug = generate_unique_slug(direction, Direction, 'name')
        direction.save()

    for subject in Subject.objects.all():
        subject.slug = generate_unique_slug(subject, Subject, 'name')
        subject.save()

class Migration(migrations.Migration):

    dependencies = [
        ('progression', '0003_remove_subjectelement_total_fragments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='slug',
            field=models.SlugField(unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(unique=True, blank=True, null=True),
        ),
        migrations.RunPython(set_unique_slugs),
        migrations.AlterField(
            model_name='direction',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
