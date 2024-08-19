# progression/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools

class Direction(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            for i in itertools.count(1):
                if not Direction.objects.filter(slug=slug).exists():
                    break
                slug = f'{base_slug}-{i}'
            self.slug = slug
        super().save(*args, **kwargs)

    def calculate_completion(self, user):
        subjects = self.subjects.all()
        total_percentage = 0
        total_elements = 0

        for subject in subjects:
            for element in subject.elements.all():
                user_progress = UserProgress.objects.filter(user=user, element=element).first()
                if user_progress:
                    total_percentage += user_progress.completion_percentage()
                total_elements += 1

        if total_elements == 0:
            return 0
        return round(total_percentage / total_elements, 2)

class Subject(models.Model):
    direction = models.ForeignKey(Direction, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    semester = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            for i in itertools.count(1):
                if not Subject.objects.filter(slug=slug).exists():
                    break
                slug = f'{base_slug}-{i}'
            self.slug = slug
        super().save(*args, **kwargs)

    def calculate_completion(self, user):
        total_percentage = 0
        total_elements = self.elements.count()
        for element in self.elements.all():
            user_progress = UserProgress.objects.filter(user=user, element=element).first()
            if user_progress:
                total_percentage += user_progress.completion_percentage()

        if total_elements == 0:
            return 0
        return round(total_percentage / total_elements, 2)

    @staticmethod
    def calculate_semester_completion(direction, semester, user):
        subjects = Subject.objects.filter(direction=direction, semester=semester)
        total_percentage = 0
        total_subjects = subjects.count()

        for subject in subjects:
            total_percentage += subject.calculate_completion(user)

        if total_subjects == 0:
            return 0
        return round(total_percentage / total_subjects, 2)

class SubjectElement(models.Model):
    subject = models.ForeignKey(Subject, related_name='elements', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    element = models.ForeignKey(SubjectElement, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_fragments = models.IntegerField(default=0)
    total_fragments = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'element')

    def completion_percentage(self):
        if self.total_fragments == 0:
            return 100
        return round((self.completed_fragments / self.total_fragments) * 100, 2)

