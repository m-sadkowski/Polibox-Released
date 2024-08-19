# progression/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Direction, Subject, SubjectElement, UserProgress
from .forms import UserProgressForm
from django.contrib.auth.decorators import login_required

def direction_list(request):
    directions = Direction.objects.all()
    direction_data = []
    for direction in directions:
        completion_percentage = direction.calculate_completion(request.user)
        direction_data.append({
            'direction': direction,
            'completion_percentage': completion_percentage,
        })
    return render(request, 'progression/direction_list.html', {'direction_data': direction_data})

def subject_list(request, direction_slug):
    direction = get_object_or_404(Direction, slug=direction_slug)
    subjects_by_semester = {}
    for semester in range(1, 8):
        subjects = Subject.objects.filter(direction=direction, semester=semester)
        subjects_with_progress = []
        for subject in subjects:
            completion_percentage = subject.calculate_completion(request.user)
            subjects_with_progress.append({
                'subject': subject,
                'completion_percentage': completion_percentage,
            })
        semester_completion = Subject.calculate_semester_completion(direction, semester, request.user)
        subjects_by_semester[semester] = {
            'subjects': subjects_with_progress,
            'completion_percentage': semester_completion,
        }
    return render(request, 'progression/subject_list.html', {
        'subjects_by_semester': subjects_by_semester,
        'direction': direction,
    })

def subject_detail(request, direction_slug, subject_slug):
    direction = get_object_or_404(Direction, slug=direction_slug)
    subject = get_object_or_404(Subject, direction=direction, slug=subject_slug)
    elements = subject.elements.all()
    user_progress = UserProgress.objects.filter(user=request.user, element__in=elements)

    progress_data = []
    for element in elements:
        progress = user_progress.filter(element=element).first()
        if progress:
            progress_percentage = progress.completion_percentage()
        else:
            progress_percentage = 0
        progress_data.append({
            'element': element,
            'progress': progress,
            'progress_percentage': progress_percentage,
        })

    subject_completion_percentage = subject.calculate_completion(request.user)

    return render(request, 'progression/subject_detail.html', {
        'subject': subject,
        'progress_data': progress_data,
        'subject_completion_percentage': subject_completion_percentage,
    })

@login_required
def update_progress(request, direction_slug, subject_slug):
    direction = get_object_or_404(Direction, slug=direction_slug)
    subject = get_object_or_404(Subject, direction=direction, slug=subject_slug)
    elements = subject.elements.all()

    if request.method == 'POST':
        for element in elements:
            user_progress, created = UserProgress.objects.get_or_create(user=request.user, element=element)
            completed_fragments = request.POST.get(f'completed_fragments_{element.id}', user_progress.completed_fragments)
            total_fragments = request.POST.get(f'total_fragments_{element.id}', user_progress.total_fragments)
            user_progress.completed_fragments = completed_fragments
            user_progress.total_fragments = total_fragments
            user_progress.save()
        return redirect('progression:subject_detail', direction_slug=direction.slug, subject_slug=subject.slug)

    return render(request, 'progression/update_progress.html', {'subject': subject, 'elements': elements})
