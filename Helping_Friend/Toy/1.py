LAB = "turtlelab3x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3x import turtle,home,shop,check

from math import degrees,atan
distShop = (shop.x**2 + shop.y**2)**0.5
angleShop = degrees(atan(abs(shop.y/shop.x)))

turtle.left(angleShop)
turtle.forward(distShop)

distHouse = ((abs(home.x - turtle.x))**2 + (abs(home.y - turtle.y))**2)**0.5
angleHouse = degrees(atan(abs(home.y - shop.y)/abs(home.x - shop.x)))

turtle.right(angleShop)
turtle.left(angleHouse)
turtle.forward(distHouse)

check()