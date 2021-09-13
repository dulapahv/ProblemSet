LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.13",LAB)

from turtlelab6 import turtle,home,flippy,rocky,check

from math import sqrt,atan2,degrees

def walkto(x,y):
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy,dx))
    turtle.left(angle-turtle.heading)
    turtle.forward(dist)

def distance(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2
    dist = sqrt(dx ** 2 + dy ** 2)
    return dist

turtleToFlippy = distance(turtle.x, turtle.y, flippy.x, flippy.y)
turtleToRocky = distance(turtle.x, turtle.y, rocky.x, rocky.y)
flippyToHome = distance(flippy.x, flippy.y, home.x, home.y)
rockyToHome = distance(rocky.x, rocky.y, home.x, home.y)

if turtleToFlippy + rockyToHome >= turtleToRocky + flippyToHome:
    walkto(rocky.x,rocky.y)
    walkto(flippy.x,flippy.y)
    walkto(home.x,home.y)
else:
    walkto(flippy.x, flippy.y)
    walkto(rocky.x, rocky.y)
    walkto(home.x, home.y)
check()