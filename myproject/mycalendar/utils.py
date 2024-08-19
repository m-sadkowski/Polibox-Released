# mycalendar/utils.py
import calendar
from .models import Event


def get_month_calendar(year, month):
    cal = calendar.Calendar(firstweekday=0)  # Create a calendar object
    month_days = cal.monthdatescalendar(year, month)  # Get the days of the month
    month_calendar = []

    for week in month_days:
        week_events = []
        for day in week:
            day_events = Event.objects.filter(date=day)  # Get all events for the day
            week_events.append({
                'day': day,  # The day object
                'events': day_events  # The events for the day
            })
        month_calendar.append(week_events)  # Append the week to the month

    return month_calendar
