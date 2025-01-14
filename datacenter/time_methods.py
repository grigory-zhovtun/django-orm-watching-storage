from datetime import timedelta, datetime


def is_visit_long(visit, minutes=60):
    visit_duration = visit.leaved_at - visit.entered_at

    if visit_duration > timedelta(minutes=minutes):
        return True
    else:
        return False

def get_duration(spent_time):
    total_seconds = int(spent_time.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    user_spent_time = datetime.timedelta(
        hours=hours, minutes=minutes, seconds=seconds
    )
    return user_spent_time


def format_duration(duration):
    return f'{duration.seconds // 3600} час {(duration.seconds // 60) % 60} мин'