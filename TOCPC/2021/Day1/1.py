# l = input()
# n,x,y = [int(x) for x in l.split()]
# batt = []
# sumx,sumy = 0,0
# for i in range(n):
#     line = input()
#     tx,ty,tc = [int(x) for x in line.split()]
#     batt.append([tx,ty,tc])
#     sumx += tx
#     sumy += ty
# if(x==0 and y == 0):
#     print(min(x[2] for x in batt))
# elif(sumx < x or sumy<y):
#     print(-1)
# else:
#     dynamic = [[[float('inf') for i in range(n)]  for j in range(y+1)] for k in range(x+1)]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(n):
#                 if(i == 0 and j == 0):
#                     dynamic[i][j][k] = 0
#                 else:
#                     if k == 0:
#                         if i <= batt[k][0] and j <= batt[k][1]:
#                             dynamic[i][j][k] = batt[k][2]
#                     else:
#                         ti = i-batt[k][0]
#                         if ti<0:
#                             ti = 0
#                         tj = j-batt[k][1]
#                         if tj<0:
#                             tj = 0
#                         dynamic[i][j][k] = min(dynamic[i][j][k-1],dynamic[ti][tj][k-1]+batt[k][2])
#                         if(ti==0 and tj ==0):
#                             dynamic[i][j][k] = min(dynamic[i][j][k],batt[k][2])
#     print(dynamic[x][y][n-1])


l = input()
n,x,y = [int(x) for x in l.split()]
batt = []
sumx,sumy = 0,0
for i in range(n):
    line = input()
    tx,ty,tc = [int(x) for x in line.split()]
    batt.append([tx,ty,tc])
    sumx += tx
    sumy += ty
if(x==0 and y == 0):
    print(min(x[2] for x in batt))
elif(sumx < x or sumy<y):
    print(-1)
else:
    dynamic = [[float('inf') for j in range(y+1)] for k in range(x+1)]

    for k in range(n):
        dynamic[0][0]= 0
        old = dynamic.copy()
        for i in range(x+1):
            for j in range(y+1):
                if i ==0 and j == 0:
                    continue
                elif (k!=0):
                    ti = i-batt[k][0]
                    if ti<0:
                        ti = 0
                    tj = j-batt[k][1]
                    if tj<0:
                        tj = 0
                    dynamic[i][j] = min(old[i][j],old[ti][tj]+batt[k][2])
                    if(ti==0 and tj ==0):
                        dynamic[i][j] = min(dynamic[i][j],batt[k][2])
                else:
                    if i <= batt[k][0] and j <= batt[k][1]:
                            dynamic[i][j] = batt[k][2]                       
    print(dynamic[x][y])