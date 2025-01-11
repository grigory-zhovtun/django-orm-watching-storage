from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from django.shortcuts import get_object_or_404


def is_visit_long(visit, minutes=60):
    visit_duration = visit.leaved_at - visit.entered_at

    if visit_duration > timedelta(minutes=minutes):
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    some_person = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=some_person)

    this_passcard_visits = []

    for visit in visits:
        current_visit_info = {
            'entered_at': visit.entered_at,
            'duration': visit.leaved_at - visit.entered_at,
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(current_visit_info)

    context = {
        'passcard': some_person,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
