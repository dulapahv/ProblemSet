import time

class Clock:
    
    ### Properties ###
    def __init__(self, hour, minute, second): #variables declaration, assume all valid inputs
        self.hour = hour
        self.minute = minute
        self.second = second
    
    ### Methods ###
    # --> SET TIME
    def set_time(self, hr, mi, se): #set time methods
        self.hour = hr
        self.minute = mi
        self.second = se

    # --> TICK (time update)
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    # --> GET TIME
    def get_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
        
    # --> DISPLAY (AM/PM)
    def displayTime(self):
        sgn = ""
        if (self.hour >= 12) and not(0 <= self.hour < 12):
            self.hour -= 12
            sgn = "PM"
        else:
            sgn = "AM"
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} {sgn}")

### CLASS CALLING, MAIN FUNCTION ###
#input debugging (actual console application) 
obj = Clock(10,49,39) #-> Valid inputs

while True:
    obj.displayTime()
    obj.tick()
    time.sleep(1)
