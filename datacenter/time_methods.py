from datetime import timedelta, datetime
from datacenter.models import Visit


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        current_duration = datetime.now() - visit.entered_at
        return current_duration > timedelta(minutes=minutes)

    visit_duration = visit.leaved_at - visit.entered_at
    return visit_duration > timedelta(minutes=minutes)


def get_spent_time(obj):
    if isinstance(obj, timedelta):
        return obj
    if isinstance(obj, Visit):
        if obj.leaved_at is None:
            return datetime.now() - obj.entered_at
        else:
            return obj.leaved_at - obj.entered_at
    raise ValueError("Unsupported type.")


def get_duration(visit):
    if visit.leaved_at is None:
        return datetime.now() - visit.entered_at
    return visit.leaved_at - visit.entered_at


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return f"{hours:02}:{minutes:02}:{seconds:02}"