from datetime import datetime, timedelta, timezone

NEPAL_TZ = timezone(timedelta(hours=5, minutes=45))


def now() -> datetime:
    now = datetime.now(NEPAL_TZ)
    return now.strftime("%Y-%m-%d %H:%M:%S")

def now_withoutstring() -> datetime:
    now_withoutstrings = datetime.now(NEPAL_TZ)
    return now_withoutstrings

print(now()) # it returns the current date and time in Nepal's timezone
