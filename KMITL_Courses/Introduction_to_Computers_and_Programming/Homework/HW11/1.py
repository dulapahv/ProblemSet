import time

class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = int(hh)
        self.mm = int(mm)
        self.ss = int(ss)
    
    def run(self):
        while True:
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
                if self.mm == 60:
                    self.mm = 0
                    self.hh += 1
                    if self.hh == 24:
                        self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            time.sleep(1)
            self.ss += 1
    
    def setTime(self, h, m, s):
        self.hh = int(h)
        self.mm = int(m)
        self.ss = int(s)


class AlarmClock(Clock):
    def __init__(self, hh, mm, ss):
        super().__init__(hh, mm, ss)
        self.alarm_hh = int(hh)
        self.alarm_mm = int(mm)
        self.alarm_ss = int(ss)
        self.alarm_on_off = False
    
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = int(h)
        self.alarm_mm = int(m)
        self.alarm_ss = int(s)
    
    def alarm_on(self):
        self.alarm_on_off = True
    
    def alarm_off(self):
        self.alarm_on_off = False
    
    def run(self):
        while True:
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
                if self.mm == 60:
                    self.mm = 0
                    self.hh += 1
                    if self.hh == 24:
                        self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            if self.ss == self.alarm_ss and self.mm == self.alarm_mm and self.hh == self.alarm_hh and self.alarm_on_off == True:
                print("Alarm! Stopping.")
                break
            else:
                time.sleep(1)
                self.ss += 1