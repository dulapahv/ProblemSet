import numpy as np

data = np.loadtxt("C:/Users/Dulapah Vibulsanti/OneDrive/Documents/GitHub/ProblemSet/HelpFriend/Pin/sales.tsv", delimiter = '    ', dtype = float)

print('Branch  Total Sale (Baht)')
Money = []
for i in data:
    Money += i[1]*1 + i[2]*5 + i[3]*10
for i in data:
    mon = np.argsort(Money)
    print(' %.f        %.f'%(i[0],mon))