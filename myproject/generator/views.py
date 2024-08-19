# generator/views.py
from django.shortcuts import render, get_object_or_404
from .models import Person
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def generator(request):
    people = Person.objects.all()
    return render(request, 'generator/generator.html', {'people': people})


@login_required(login_url="/users/login/")
def generate_text(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    greeting_text = person.greeting + ', '
    mail_text = person.mail
    return JsonResponse({'greeting_text': greeting_text, 'mail_text': mail_text})
