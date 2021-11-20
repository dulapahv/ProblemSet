class Clock:
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def set_time(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def get_time(self):
        sign = "AM"
        if 12 < self._hour < 24:
            self._hour -= 12
            sign = "PM"
        elif self._hour == 24:
            self._hour = 0
        else:
            if self._hour == 12 and sign == "PM":
                self._hour = 0
                sign = "AM"
        print(f"{self._hour:02d}:{self._minute:02d}:{self._second:02d} {sign}")

    def tick(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def setHour(self, hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            return "Invalid hour value"

    def setMinute(self, minute):
        if 0 <= minute < 60:
            self._minute = minute
        else:
            return "Invalid minute value"

    def setSecond(self, second):
        if 0 <= second < 60:
            self._second = second
        else:
            return "Invalid second value"