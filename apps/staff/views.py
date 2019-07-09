from django.shortcuts import render

# Create your views here.
from apps.content.models import Event
from apps.staff.models import Staff


def staff(request, event_id = None):
    events = list(Event.objects.all())
    x = []
    for e in events:
        x.append({
            'id': e.id,
            'persian_name': e.persian_name,
            'english_name': e.english_name
        })
    context = {'events': x}
    if event_id is not None:
        active = Event.objects.get(id=event_id)
    else:
        if len(events) > 0:
            active = events[len(events)-1]
        else:
            active = None
    if active is not None:
        staffs = list(Staff.objects.filter(event=active))
        ctx = {
            'id': active.id,
            'staff': staffs
        }
        context.update({
            'active': ctx
        })
    return render(request, 'staff/staff.html', context)

