from django.shortcuts import render

from .models import *
from apps.content.models import Event


def scoreboard(request, event_id=None):
    if event_id is not None and Event.objects.filter(pk=event_id).count() == 1:
        event = Event.objects.get(pk=event_id)
    elif Event.objects.count() > 0:
        event = Event.objects.order_by('-year').first()
    else:
        return render(request, 
                'scoreboard/scoreboard.html',
                context={"error": "No Events Yet!"})

    context = {
        'events': list(Event.objects.order_by('-year')),
        'event': event,
        'contest_tiers': [
                {
                    'tr': tier,
                    'table_header': 
                        ['Name', 'Country', ] \
                        + ["P" + str(sc.p_id) for sc in ProblemScore.objects.filter(contestant=Contestant.objects.first(event_tier=tier)).order_by('p_id')] \
                        + ['Score', 'Rank', 'Ruler'],
                    'contestants': [
                            {
                                'con': con,
                                'scores': ProblemScore.objects.filter(contestant=con).order_by('p_id'),
                                'sum_score': sum(list(ProblemScore.objects.filter(contestant=con))),
                            }
                        for con in Contestant.objects.filter(event_tier=tier).order_by('rank')],
                }
            for tier in ContestTier.objects.filter(event__id=event.id)]
    }

