from django.shortcuts import render

from .models import *

from random import shuffle


def gallery(request, event_id=None):
    if event_id is not None and Event.objects.filter(pk=event_id).count() == 1:
        event = Event.objects.get(pk=event_id)
    elif Event.objects.count() > 0:
        event = Event.objects.order_by('-year').first()
    else:
        return render(request, 
                'gallery/gallery.html',
                context={"error": "No Events Yet!"})

    context = {
        'events': list(Event.objects.order_by('year')),
        'event': event,
        'by_country_event_images': [
            {
                'coev': coev,
                'images': shuffle(list(Image.objects.filter(country_event=coev))),
            } for coev in CountryEvent.objects.filter(event=event).order_by('country__name')],
    }

    return render(request, 'gallery/gallery.html', context)

