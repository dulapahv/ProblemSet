def read_vector(msg):
    print(msg)
    x = float(input("x = "))
    y = float(input("y = "))
    return x,y

def dot_product(x1,y1,x2,y2):
    return (x1 * x2) + (y1 * y2)

x1, y1 = read_vector("Enter vector A")
x2, y2 = read_vector("Enter vector B")
print(f"Dot product of A and B is {dot_product(x1, y1, x2, y2):.2f}")