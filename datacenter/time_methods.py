from datetime import timedelta, datetime


def is_visit_long(visit, minutes=60):
    visit_duration = visit.leaved_at - visit.entered_at

    if visit_duration > timedelta(minutes=minutes):
        return True
    else:
        return False

def get_duration(spent_time):
    if not isinstance(spent_time, timedelta):
        raise ValueError("Input must be a timedelta object")
    total_seconds = int(spent_time.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    result = []
    if days > 0:
        result.append(f"{days} дн")
    if hours > 0 or days > 0:  # Если есть дни, то часы выводим всегда
        result.append(f"{hours} час")
    result.append(f"{minutes} мин")

    return ' '.join(result)