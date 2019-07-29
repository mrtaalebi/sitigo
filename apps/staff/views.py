from django.shortcuts import render

from apps.content.models import Event
from apps.staff.models import Staff

import random


def staff(request, event_id = None):
    events = Event.objects.all().order_by('year')
    if event_id is not None and events.filter(pk=event_id).count() == 1:
        active = events.get(pk=event_id)
    elif events.count() > 0:
        active = events.last()
    else:
        return render(reqeust, 'staff/staff.html', context={'events': events})

    e_staff = Staff.objects.filter(event=active)
    role_tiers = set()
    for s in e_staff:
        role_tiers.add(s.role.tier)
    role_tiers = sorted(list(role_tiers), key=lambda x : x.position_from_top)
    context = {
        'events': events,
        'active': active,
        'tiers' :[{
            't': t,
            'staff': e_staff.filter(role__tier=t)
        } for t in role_tiers]
    }

    for tier in context['tiers']:
        random.shuffle(tier['staff'])

    return render(request, 'staff/staff.html', context)

