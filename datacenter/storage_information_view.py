from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import locale
from time_methods import get_duration, format_duration


def storage_information_view(request):
    persons_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    current_time = localtime()

    non_closed_visits = []
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    for visit in persons_not_leaved:
        et = localtime(visit.entered_at)
        non_closed_visits.append({
            'who_entered': Passcard.objects.get(owner_name=visit.passcard),
            'entered_at': et.strftime('%d %B %Y г. %H:%M'),
            'duration': format_duration(get_duration(current_time - et))
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
