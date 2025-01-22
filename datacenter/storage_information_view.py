from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import locale
from datacenter.time_methods import get_duration, format_duration


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)
    current_time = localtime()

    non_closed_visits = []
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    for visit in unclosed_visits:
        entered_time = localtime(visit.entered_at)
        duration = current_time - entered_time
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,  # или просто visit.passcard
            'entered_at': entered_time.strftime('%d %B %Y г. %H:%M'),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
