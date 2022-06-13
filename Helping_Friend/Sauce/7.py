# HW
# By using the skeleton of code below.

def get_day_week(d, m, y):
    day_of_week = ['Monday', 'Tuesday', 'Wednesday',
                   'Thursday', 'Friday', 'Saturday', 'Sunday']  
    ### BEGIN SOLUTION
    
    pass 
    if (m < 3):
        m += 12
        y -= 1

        c = y//100
        k = y % 100
        w = (d + (26*(m+1))//10 + k + k//4 + c//4 - 2*c) % 7
    
        if w == 0:
            return day_of_week[5]
        elif w == 1:
            return day_of_week[6]
        elif w == 2:
            return day_of_week[0]
        elif w == 3:
            return day_of_week[1]
        elif w == 4:
            return day_of_week[2]
        elif w == 5:
            return day_of_week[3]
        else:
            return day_of_week[4]

          
    ### END SOLUTION


d = int(input("Date  = "))
m = int(input("Month Number = "))
y = int(input("Year (A.D.) = "))

print(get_day_week(d, m, y))