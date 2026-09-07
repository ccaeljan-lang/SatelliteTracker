from datetime import timezone, datetime


def convertTime(timestamp):
    time = datetime.fromtimestamp(timestamp, timezone.utc)
    return time
