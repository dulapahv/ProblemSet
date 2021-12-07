class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def setTime(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d} Hrs."


class TimeSettingError(RuntimeError):
    def __init__(self, h, m, s):
        super().__init__(h, m, s)

    def check_time(self):
        if 0 > self.h >= 24 and 0 > self.m >= 60 and 0 > self.s >= 60:
            raise TimeSettingError


time1 = TimeSettingError(9, 61, 0)
print(time1)