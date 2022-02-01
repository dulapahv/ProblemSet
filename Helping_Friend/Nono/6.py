usin = int(input())

GIGA = 10**9
MEGA = 10**6
KILO = 10**3

if len(str(usin)) >= len(str(GIGA)):
    usin /= GIGA
    print(f"{int(usin)}G") if usin % 1 == 0 else print(f"{round(usin, 1)}G")
elif len(str(usin)) >= len(str(MEGA)):
    usin /= MEGA
    print(f"{int(usin)}M") if usin % 1 == 0 else print(f"{round(usin, 1)}M")
elif len(str(usin)) >= len(str(KILO)):
    usin /= KILO
    print(f"{int(usin)}K") if usin % 1 == 0 else print(f"{round(usin, 1)}K")
else:
    print(usin)