x=int(input("Enter an integer:"))
print("your Sum=",(x))

y=int(input("Enter an integer:"))
y2=y+x
if x>=0:
    if y<0:
        print("your Sum=",(y))
    else:
        print("your Sum=",(y2))
if x<0:
    if y>=0:
         print("your Sum=",(y))
    else:
        print("your Sum=",(y2))

z=int(input("Enter an integer:"))
z2=z+y2
if y2>=0:
    if z<0:
        print("your Sum=",(z))
    else:
        print("your Sum=",(z2))
if y2<0:
    if z>=0:
         print("your Sum=",(z))
    else:
        print("your Sum=",(z2))

a=int(input("Enter an integer:"))
a2=z2+a
if z2>=0:
    if a<0:
        print("your Sum=",(a))
    else:
        print("your Sum=",(a2))
if z2<0:
    if a>=0:
         print("your Sum=",(a))
    else:
        print("your Sum=",(a2))

b=int(input("Enter an integer:"))
b2=a2+b
if a2>=0:
    if b<0:
        print("your Sum=",(b))
    else:
        print("your Sum=",(b2))
if a2<0:
    if b>=0:
         print("your Sum=",(b))
    else:
        print("your Sum=",(b2))