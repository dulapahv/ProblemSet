from datetime import datetime
from random import choice


def get_day_week(d,m,y):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date = datetime(y,m,d)
    return days[date.weekday()]


test_N = 5

for i in range(test_N):
    # สุ่มโดยเช็คปีว่าเป็นปี leap-year หรือไม่ และกำหนดจำนวนวันของแต่ละเดือน เพื่อไม่ให้วันที่เกิน 
    years = list(range(1950, 2101)) # years 1950~2100
    y = choice(years)
    # Check for leap-year
    if (((y % 4 == 0) and (y % 100 != 0))) or (y % 400 == 0):
        leap_flag = True
    else:
        leap_flag = False

    months = list(range(1, 12)) # 12 months list
    m = choice(months)
    if m in (1, 3, 5, 7, 8, 10, 12):
        m_length = 31
    elif m == 2:
        if leap_flag:
            m_length = 29
        else:
            m_length = 28
    else:
        m_length = 30

    dates = list(range(1, m_length)) 
    d = choice(dates)

    print('{}/{}/{}'.format(d, m, y), end=' ')
    ans = datetime(y,m,d).date().strftime('%A')
    ans_flag = (get_day_week(d,m,y) == ans)
    print('-> {} \t {}'.format(d, ans_flag))