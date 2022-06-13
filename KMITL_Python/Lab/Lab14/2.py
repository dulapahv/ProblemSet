import time

class TimeSettingError(RuntimeError):
    pass

class Time:
    def __init__(self, hh, mm, ss):
        try:
            self.hh = int(hh)
            self.mm = int(mm)
            self.ss = int(ss)
            if not (0 <= hh <= 23) or not (0 <= mm <= 59) or not (0 <= ss <= 59):
                raise TimeSettingError
        except TimeSettingError:
            print("Time setting error!")
            exit(1)
       
    def setTime(self, h, m, s):
        try:
            self.hh = h
            self.mm = m
            self.ss = s
            if not (0 <= h <= 23) or not (0 <= m <= 59) or not (0 <= s <= 59):
                raise TimeSettingError
        except TimeSettingError:
            print("Time setting error!")
    
    def __str__(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d} Hrs."

time1 = Time(9,50,0)
print(time1)

