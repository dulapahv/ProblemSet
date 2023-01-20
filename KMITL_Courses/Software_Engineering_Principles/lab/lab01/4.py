class Time:
    def __init__(self, hour, minute, second) -> None:
        if hour < 0 or hour >= 24:
            raise ValueError('hour must be in 0-23')
        if minute < 0 or minute >= 60:
            raise ValueError('minute must be in 0-59')
        if second < 0 or second >= 60:
            raise ValueError('second must be in 0-59')
        self.hour = hour
        self.minute = minute
        self.second = second

    def setTime(self, hour, minute, second) -> None:
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be 0-23")
        if minute < 0 or minute > 59:
            raise ValueError("Minute must be 0-59")
        if second < 0 or second > 59:
            raise ValueError("Second must be 0-59")
        self.hour = hour
        self.minute = minute
        self.second = second

    def getTime(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} Hrs."

    def print(self) -> None:
        print(self.getTime())


time1 = Time(9, 30, 0)
time1.print()
