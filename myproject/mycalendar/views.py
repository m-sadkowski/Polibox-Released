# mycalendar/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event
from .forms import EventForm
from datetime import date, timedelta
import calendar
from .utils import get_month_calendar


def is_admin(user):
    return user.is_superuser


@login_required(login_url='/users/login/')
def calendar_view(request):
    year = int(request.GET.get('year', date.today().year))
    month = int(request.GET.get('month', date.today().month))

    # Get the current calendar
    context = {'calendar': get_month_calendar(year, month),
               'events': Event.objects.filter(date__year=year, date__month=month)}

    # Calculate previous and next month
    first_day_of_month = date(year, month, 1)
    prev_month_last_day = first_day_of_month - timedelta(days=1)
    next_month_first_day = first_day_of_month + timedelta(days=calendar.monthrange(year, month)[1])

    context['prev_month'] = prev_month_last_day.month
    context['prev_month_year'] = prev_month_last_day.year
    context['next_month'] = next_month_first_day.month
    context['next_month_year'] = next_month_first_day.year

    # Add the name of the current month
    context['current_month_name'] = first_day_of_month.strftime('%B %Y')

    return render(request, 'mycalendar/calendar.html', context)


@user_passes_test(is_admin, login_url='/users/login/')
@csrf_exempt
@require_http_methods(["GET", "POST"])
def event_create_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mycalendar:calendar')
    else:
        event_date = request.GET.get('date')
        form = EventForm(initial={'date': event_date})

    return render(request, 'mycalendar/event_form.html', {'form': form})


@user_passes_test(is_admin, login_url='/users/login/')
def event_delete_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('mycalendar:calendar')


@user_passes_test(is_admin, login_url='/users/login/')
@csrf_exempt
@require_http_methods(["GET", "POST"])
def event_update_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('mycalendar:calendar')
    else:
        form = EventForm(instance=event)

    return render(request, 'mycalendar/event_form.html', {'form': form})
