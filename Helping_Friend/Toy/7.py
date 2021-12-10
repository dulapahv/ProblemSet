def rev(s):
    r1 = ''
    r2 = ''
    for i in range(len(s)):
        r1 = r1 + s[len(s)-i-1]
    for i in range(1,len(s)):
        r2 = r2 + r1[i]
    return r2

s = input()
r = ''
for i in range(len(s)):
    r = r + s[i]
    res = f'{r}{rev(r)}'
    print(f'{" "*(len(s)-i-1)}{res}')