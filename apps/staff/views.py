from django.shortcuts import render
from django.db.models import Q
from apps.content.models import Event
from apps.staff.models import Team, Role, Staff

import random


def staff(request, event_id = None):
    events = Event.objects.all().order_by('year')
    if event_id is not None and events.filter(pk=event_id).count() == 1:
        active = events.get(pk=event_id)
    elif events.count() > 0:
        active = events.last()
    else:
        return render(request, 'staff/staff.html', context={'events': events})

    context = {
        'events': events,
        'active': active,
        'teams' :[{
            't': t,
            'staff_persian_sorted': list(Staff.objects.filter(role__team=t, role__is_head=False).order_by('persian_lastname')),
            'staff_english_sorted': list(Staff.objects.filter(role__team=t, role__is_head=False).order_by('english_lastname')),
            'heads_persian_sorted': list(Staff.objects.filter(role__team=t, role__is_head=True).order_by('persian_lastname')),
            'heads_english_sorted': list(Staff.objects.filter(role__team=t, role__is_head=True).order_by('english_lastname')),
        } for t in Team.objects.filter(event=active).order_by('position_from_top')]
    }

    return render(request, 'staff/staff.html', context)

