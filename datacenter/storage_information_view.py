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
        entered_time = localtime(visit.entered_at)
        time_spent = current_time - entered_time
        entered_time_str = entered_time.strftime('%d %B %Y г. %H:%M')

        duration = get_duration(time_spent)
        str_duration = format_duration(duration)

        # Вывод сообщений
        owner = visit.passcard
        person = Passcard.objects.get(owner_name=owner)

        current_closed_visit = {
            'who_entered': person,
            'entered_at': entered_time_str,
            'duration': str_duration,
        }
        non_closed_visits.append(current_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
