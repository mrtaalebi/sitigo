from django.shortcuts import render

# Create your views here.
from apps.content.models import Age
from apps.staff.models import Staff


def staff(request):
    events = list(Age.objects.all())
    x = []
    for e in events:
        x.append({
            'id': e.id,
            'persian_name': e.persian_name,
            'english_name': e.english_name
        })
    context = {'events': x}
    if request.method == 'POST':
        active = Age.objects.get(id=request.POST.get('id', 1))
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

