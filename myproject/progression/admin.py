# progression/admin.py
from django.contrib import admin
from .models import Direction, Subject, SubjectElement, UserProgress

class SubjectElementInline(admin.TabularInline):
    model = SubjectElement

class SubjectAdmin(admin.ModelAdmin):
    inlines = [SubjectElementInline]

admin.site.register(Direction)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectElement)
admin.site.register(UserProgress)
