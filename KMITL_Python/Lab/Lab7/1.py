class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print(self):
        if self.hour < 0:
            self.hour = 0
        elif self.hour > 24:
            self.hour = 24
        if self.minute < 0:
            self.minute = 0
        elif self.minute > 60:
            self.minute = 60
        if self.second < 0:
            self.second = 0
        elif self.second > 60:
            self.second = 60
        print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")