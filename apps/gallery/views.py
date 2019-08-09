from django.shortcuts import render
from django.utils import translation

from .models import *

from random import shuffle


def gallery(request, event_id=None, gallery_id=None):
    if event_id is not None and Event.objects.filter(pk=event_id).count() == 1:
        event = Event.objects.get(pk=event_id)
    elif Event.objects.count() > 0:
        event = Event.objects.order_by('-year').first()
    else:
        return render(request, 
                'gallery/gallery.html',
                context={"error": "No Events Yet!"})

    if gallery_id is not None and Gallery.objects.filter(event=event, id=gallery_id).count() == 1:
        gallery = Gallery.objects.get(event=event, id=gallery_id)
    else:
        gallery = None

    context = {
        'events': list(Event.objects.order_by('year')),
        'event': event,
        'gallery_links': [{
            'g': g,
            'link': '/gallery/{}/{}'.format(event.id, g.id) 
            } for g in Gallery.objects.filter(event=event)]
            + [{'g': 
                    {
                        'persian_name': 'سراسر جهان',
                        'english_name': 'World Wide'
                    },
                'link': '/gallery/{}/'.format(event.id)
                }] if event.id != 1 else [],
        'gallery_english_name': gallery.english_name if gallery is not None \
                else 'World Wide' if event.id != 1 else 'Iran'
    }

    if translation.get_language() == "fa":
        sort_by = "country__persian_name"
    else:
        sort_by = "country__english_name"

    context['by_country_event_images'] = [
        {
            'coev': coev,
            'images': list(Image.objects.filter(country_event=coev)),
        } for coev in CountryEvent.objects.filter(event=event, gallery=gallery).order_by(sort_by)
    ]
    
    import random
    for imgs in context['by_country_event_images']:
        random.shuffle(imgs['images'])

    return render(request, 'gallery/gallery.html', context)

