def to_twelve_hour(time):
    hour, minute = time.split(":")
    if int(hour) > 12:
        hour = int(hour) - 12;
    if int(hour) >= 12:
        return (f"{hour}:{minute} PM")
    else:
        return (f"{hour}:{minute} AM")