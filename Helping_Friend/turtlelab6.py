"""
Turtle Lab Module
=================

Provides an interactive problem solving environment based on Python's turtle graphics

AUTHOR

Chaiporn (Art) Jaikaeo
Intelligent Wireless Networking Group (IWING) -- http://iwing.cpe.ku.ac.th
Department of Computer Engineering
Kasetsart University
chaiporn.j@ku.ac.th
"""
import sys
import os
import inspect
import importlib.util
import pathlib
from types import ModuleType
from textwrap import dedent
from math import sin,cos,radians,sqrt
from collections import namedtuple

# make sure there is no file named 'turtle.py' inside student's working
# directory
#if pathlib.Path("turtle.py").exists():
#    print("ERROR: A file named 'turtle.py' is detected in your working directory.")
#    print("Please remove or rename it; otherwise the task will not work correctly.")
#    sys.exit(1)

# make sure there is no directory named 'turtle' inside student's working
# directory
#if pathlib.Path("turtle").is_dir():
#    print("ERROR: A directory named 'turtle' is detected in your working directory.")
#    print("Please remove or rename it; otherwise the task will not work correctly.")
#    sys.exit(1)

try:
    INTERACTIVE = (os.environ['ELAB_GRADING'] != '1')
except KeyError:
    INTERACTIVE = True

if INTERACTIVE:
    try:
        # remove the current path out of sys.path to prevent a local turtle.py
        # module to be accidentally imported
        syspath = sys.path
        sys.path = sys.path[1:]

        # make sure 'turtle' module exists before loading
        turtle_spec = importlib.util.find_spec("turtle")
        if turtle_spec is None:
            print(f"ERROR: Standard 'turtle' module not found")
            sys.exit(1)

        try:
            import turtle as std_turtle
        except ImportError as e:
            std_turtle = None
        sys.path = syspath
        
        # make sure 'std_turtle' is indeed the genuine Turtle library
        # (now just check whether there is a Canvas class inside the tkinter
        # module)
        if std_turtle is None or \
           not 'Canvas' in std_turtle.__dict__ or \
           not inspect.isclass(std_turtle.Canvas) or \
           not std_turtle.Canvas.__module__ == 'tkinter':
            print(f"ERROR: Invalid turtle module is found in {turtle_spec.origin}")
            print("Please remove it and rerun the script.")
            sys.exit(1)

        import base64
        from io import BytesIO
        INTERACTIVE = True
        SCREEN_SIZE_X = 1200
        SCREEN_SIZE_Y = 1200
    except ModuleNotFoundError:
        INTERACTIVE = False
        std_turtle = None
    try:
        from PIL import Image,ImageTk
    except ModuleNotFoundError:
        Image = None
        ImageTk = None


#############################
class array(list):
    def __init__(self,elements):
        list.__init__(self,elements)

    def __add__(self,value):
        if isinstance(value,array):
            return array([x+y for x,y in zip(self,value)])
        if isinstance(value,(int,float)):
            return array([x+value for x in self])

    def __radd__(self,value):
        return self.__add__(value,self)

    def __sub__(self,value):
        if isinstance(value,array):
            return array([x-y for x,y in zip(self,value)])
        if isinstance(value,(int,float)):
            return array([x-value for x in self])

    def __rsub__(self,value):
        if isinstance(value,array):
            return array([y-x for x,y in zip(self,value)])
        if isinstance(value,(int,float)):
            return array([value-x for x in self])

    def __mul__(self,value):
        if isinstance(value,array):
            return array([x*y for x,y in zip(self,value)])
        if isinstance(value,(int,float)):
            return array([x*value for x in self])

    def __rmul__(self,value):
        return self.__mul__(value,self)

    def __truediv__(self,value):
        if isinstance(value,(int,float)):
            return array([x/value for x in self])
        else:
            raise Exception("Unsupported operation")

    def __neg__(self,value):
        return array([-x for x in self])

#############################
def inner(u,v):
    return sum(a*b for a,b in zip(u,v))

#############################
def norm(v):
    return sqrt(sum(x*x for x in v))

#############################
def closest_point_on_seg(seg_p1, seg_p2, pos):
    """
    Return the point on the segment given by two endpoints, seg_p1 and seg_p2,
    closest to the point pos

    Taken from:
      http://doswa.com/2009/07/13/circle-segment-intersectioncollision.html
    """
    seg_v = seg_p2 - seg_p1
    pt_v = pos - seg_p1
    if norm(seg_v) <= 0:
        raise ValueError("Invalid segment length")
    seg_v_unit = seg_v / norm(seg_v)
    proj = inner(pt_v,seg_v_unit)
    if proj <= 0:
        return seg_p1
    if proj >= norm(seg_v):
        return seg_p2
    return seg_v_unit*proj + seg_p1

#############################
class Point(namedtuple("Point","x y")):
    pass

#############################
class Line(namedtuple("Line","x1 y1 x2 y2")):
    pass

#############################
class Circle(namedtuple("Circle","x y radius")):

    def intersects(self,p1:Point,p2:Point)->bool:
        """
        Determine whether the line from the point p1 to the point p2 intersects
        this circle
        """
        circ_pos = array([self.x,self.y])
        closest = closest_point_on_seg(
                array([p1.x,p1.y]),
                array([p2.x,p2.y]),
                circ_pos)
        dist_v = circ_pos - closest
        return norm(dist_v) <= self.radius

#############################
class Rectangle(namedtuple("Rectangle","x y width height")):

    def contains(self,p:Point)->bool:
        """
        Determine whether this rectangle contains the point p
        """
        return (((self.x-self.width/2) < p.x < (self.x+self.width/2)) and 
                ((self.y-self.height/2) < p.y < (self.y+self.height/2)))

#############################
class Turtle:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._heading = 0
        self.allow_negative_distance = False
        self.pos_changed_callbacks = []
        self.dir_changed_callbacks = []

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def position(self):
        return Point(self._x,self._y)

    @property
    def heading(self):
        return self._heading

    def reset(self):
        self._x = 0
        self._y = 0
        self._heading = 0
        self.pos_changed_callbacks.clear()
        self.dir_changed_callbacks.clear()

    def _forward(self,distance):
        old_pos = self.position
        rad = radians(self._heading)
        self._x += distance*cos(rad)
        self._y += distance*sin(rad)
        if distance != 0:
            for callback in self.pos_changed_callbacks:
                callback(self,old_pos,self.position,abs(distance))

    def forward(self,distance):
        if not self.allow_negative_distance and distance<0:
            raise Exception("Negative distance is not allowed")
        self._forward(distance)

    def backward(self,distance):
        if not self.allow_negative_distance and distance<0:
            raise Exception("Negative distance is not allowed")
        self._forward(-distance)

    def left(self,angle):
        old_dir = self.heading
        self._heading = ((self._heading+angle)%360 + 360) % 360;
        if old_dir != self.heading:
            for callback in self.dir_changed_callbacks:
                callback(old_dir,self.heading)

    def right(self,angle):
        old_dir = self.heading
        self._heading = ((self._heading-angle)%360 + 360) % 360;
        if old_dir != self.heading:
            for callback in self.dir_changed_callbacks:
                callback(self,old_dir,self.heading)

    def done(self):
        pass

#############################
class TurtleGui(Turtle):
    def __init__(self):
        super(TurtleGui,self).__init__()
        self.canvas = std_turtle.getcanvas()
        std_turtle.setup()
        std_turtle.screensize(SCREEN_SIZE_X,SCREEN_SIZE_Y,"white")
        std_turtle.shape("turtle")
        std_turtle.color("#00AA00")
        std_turtle.pencolor("darkgreen")
        std_turtle.pensize(5)
        self.reset()

    def reset(self):
        super(TurtleGui,self).reset()
        std_turtle.penup()
        std_turtle.home()
        std_turtle.clear()
        std_turtle.pendown()

    def forward(self,distance):
        super(TurtleGui,self).forward(distance)
        std_turtle.forward(distance)

    def backward(self,distance):
        super(TurtleGui,self).backward(distance)
        std_turtle.backward(distance)

    def left(self,angle):
        super(TurtleGui,self).left(angle)
        std_turtle.left(angle)

    def right(self,angle):
        super(TurtleGui,self).right(angle)
        std_turtle.right(angle)

    def done(self):
        std_turtle.done()

#############################
class Stage:
    def __init__(self,gui=False):
        self.gui = gui
        if gui:
            self.turtle = TurtleGui()
            self.canvas = self.turtle.canvas
            self.draw_grid()
        else:
            self.turtle = Turtle()
        self.objects = []
        self.stops = []
        self.reset()

    def reset(self):
        self.turtle.reset()
        self.objects.clear()
        self.stops.clear()
        self.stops.append(self.turtle.position)
        self.turtle.pos_changed_callbacks.append(self.add_stop)
        if self.gui:
            self.canvas.delete("object")

    def add_stop(self,turtle,opos,npos,dist):
        self.stops.append(npos)

    def add_object(self,obj):
        self.objects.append(obj)
        if self.gui:
            item = obj.draw(self.canvas)
            if hasattr(item,"__iter__"):
                for it in item:
                    self.canvas.itemconfig(it,tags="object")
                    self.canvas.tag_lower(it)
            else:
                self.canvas.itemconfig(item,tags="object")
                self.canvas.tag_lower(item)
            self.canvas.tag_lower("grid")

    def draw_grid(self):
        rounded_x = int(round(SCREEN_SIZE_X/2,-2))
        rounded_y = int(round(SCREEN_SIZE_Y/2,-2))
        for i in range(-rounded_x,rounded_y,100):
            fill = "black" if i==0 else "grey"
            self.canvas.create_line(
                    -rounded_x,i,rounded_x,i,fill=fill,tags="grid")
            self.canvas.create_line(
                    i,-rounded_y,i,rounded_y,fill=fill,tags="grid")
        self.canvas.tag_lower("grid")

    def recenter(self,x,y):
        if self.gui:
            print(x,y)
            self.canvas.xview_scroll(x,"units")
            self.canvas.yview_scroll(-y,"units")

#############################
class Boulder(Circle):
    def __new__(cls,x,y,diameter,image=None):
        self = super(Boulder,cls).__new__(cls,x,y,diameter/2)
        self.image = image
        return self

    def draw(self,canvas):
        if self.image is None or ImageTk is None:
            item = canvas.create_oval(
                    self.x - self.radius,
                   -self.y - self.radius,
                    self.x + self.radius,
                   -self.y + self.radius,
                    fill="brown")
        else:
            image = Image.open(BytesIO(base64.b64decode(self.image)))
            image = image.resize((int(self.radius*2),int(self.radius*2)),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(image)
            item = canvas.create_image(self.x,-self.y,image=self.photo)
        canvas.itemconfig(item,tags="boulder")
        return item


#############################
class Home(Rectangle):
    def __new__(cls,x,y,width,height,image=None,text=""):
        self = super(Home,cls).__new__(cls,x,y,width,height)
        self.image = image
        self.text = text
        return self

    def draw(self,canvas):
        if self.image is None or ImageTk is None:
            item = canvas.create_rectangle(
                    self.x - self.width/2,
                   -self.y - self.height/2,
                    self.x + self.width/2,
                   -self.y + self.height/2,
                    fill="blue")
        else:
            image = Image.open(BytesIO(base64.b64decode(self.image)))
            image = image.resize((self.width,self.height),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(image)
            item = canvas.create_image(self.x,-self.y,image=self.photo)
        item_txt = canvas.create_text(self.x,-self.y+self.height/2+5,text=self.text)
        canvas.itemconfig(item_txt,tags="home")
        return item,item_txt

#############################
class Road(Line):
    def __new__(cls,x1,y1,x2,y2,width,color):
        self = super(Road,cls).__new__(cls,x1,y1,x2,y2)
        self.width = width
        self.color = color
        return self

    def draw(self,canvas):
        item = canvas.create_line(
                self.x1,-self.y1,self.x2,-self.y2,
                width=self.width,
                fill=self.color,
                capstyle="round")
        canvas.itemconfig(item,tags="road")
        return item

#############################
IMG_BOULDER = """
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
"""

IMG_HOME = """
R0lGODlhQABAAOf/AKQCAKsAAK0AAawACaUEBa8CA6YGALkACa8EC7EHDagLB7IKBbwHC6oQEcgJE7UQ
ELURF60VGcERD8ESF9YQG5IkJs0VF6sfGrwbFcUZGb0dHM8YH60iIdoYHrgjIdIcGskfHcAiJbEnKtMe
Id0dIOcbHsQmIdUhI+ccJdYiHa4tKs4lIN8gKNcjJI03Oc4mJuofIOAiItglJeohJ+IkJNonJsEuLrMy
M+MmJcouMu0lKeUoJu8nJLE5Ot4tL/ApJc8yL9YwMvApK9E1N1ZYVe4zMrpBQeU2O9A9PlxdW+A6OS5l
p9k9PPE3NbhHR/I4Ozponj1opdhFROBDQfBAPPBBQmVnZFBpkLpRUupERk9sjEJtqvNDRNdNTN9MT7lX
VD5zr+FNSnVqa/FLTG5wbUp2rfROTu1QUXFzcHZycG90dm11fHN1cupWV/JUVFB7s3N3enB4f8FkY+Va
XeBcW3d5dvVXV75oZHB8iG58jnl7eHp8eb5qa2F/rVyAs3WAjfRfX42DLH+BfvdhYfFjX+tlZFqIuWOH
un+Eh4KEgZOIKoOFgpCIP2iJsWOKtvRnaISGg46HXYmIboeHfoWHhPZpaoiJdIyJaYaIhcZ3dYeJhoiK
h8J6fPRua4mLiG6PtmqQvYqMifZwc4yOi22TwMd/gY6QjfV2dXCWw6qZAKuaB56XUvh5eMiGhXmZwqOc
NZWXlPV+f3ucxMeMiH6fx5qcmZ+hntGWmKSmos6bmrWipKWnpMaxAM2gncWxEKmrp62vrNWnpLizstGt
rbW3tNGzsrm7uNiztL+6udS2tcK9u72/u8DCv8vFxMXHxMbIxdHFxeDCwNjExt7HxMzOy9nMzM7QzM/R
ztDSz9fR0NLU0dPV0tTW0+DT09XX1NvW1NbY1d3X1tja1uTX19nb19rc2eDb2dvd2uLc29ze293f3N7g
3d/h3uXg3uDi3+Hk4OPl4erk4+Tm4+Xn5Obo5efp5ujq5+nr6Ovt6u3v7O/x7vDy7/L08fX39Pj69///
/yH5BAEKAP8ALAAAAABAAEAAAAj+AP8JHEiwoMGDCBMqXMiwocOHECMeNCCxosWCBgRQvMgRogEJOCRs
7EgSoQEDG540CTmypMt/GU9QeVJkBg4HAVq+vGgggY8qVagUQYEDh4WcOzkaeHCEC9AqRYoWPaozqUMD
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
CQgAOw==
"""

stage = Stage(gui=INTERACTIVE)

def verify_turtle():
    """
    Ensure that the 'turtle' variable in the main module is referring to the
    turtle object created by this module
    """
    try:
        # stack[0] -> verify_turtle()
        # stack[1] -> done()
        # stack[2] -> student's code
        submission_turtle = inspect.stack()[2].frame.f_locals["turtle"]
    except KeyError:
        submission_turtle = None
    if submission_turtle is not stage.turtle:
        print("ERROR: YOU ARE USING A WRONG TURTLE.")
        print("Please make sure that 'import turtle' is NOT used")
        sys.exit(1)

def submitted_byte_count():
    """
    Return the number of bytes in the main code to be submitted.  If this
    function is called from a shell, -1 is returned.
    """
    try:
        submitted_file = inspect.getfile(inspect.stack()[-1].frame)
        return os.stat(submitted_file).st_size
    except FileNotFoundError:
        return -1

def submitted_line_count():
    """
    Return the number of lines in the main code to be submitted.  If this
    function is called from a shell, -1 is returned.
    """
    try:
        submitted_file = inspect.getfile(inspect.stack()[-1].frame)
        with open(submitted_file) as f:
            return len(f.readlines())
    except FileNotFoundError:
        return -1

from random import choice,randint,shuffle
from math import sqrt

#############################
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

#############################
class Task:
    """
    TASK: help guide Turtle back home while stop to visit Flippy and
    Rocky Flippy's, Rocky's, and Turtle's home will randomly appear
    ANYWHERE on the map.
    """
    def start(self):
        stage.reset()
        stage.turtle.pos_changed_callbacks.append(self.pos_changed)

        if INTERACTIVE:
            locations = [
                (+randint(100,200),+randint(100,200)),
                (+randint(100,200),-randint(100,200)),
                (-randint(100,200),+randint(100,200)),
                (-randint(100,200),-randint(100,200)),
            ]
            shuffle(locations)
            locations = locations[:2]
            home_x,home_y = locations[0]
            home_x += choice([-1,1])*randint(50,100)
            home_y += choice([-1,1])*randint(50,100)
            shuffle(locations)
            (flippy_x,flippy_y),(rocky_x,rocky_y) = locations
        else:
            flippy_x,flippy_y = int(input()),int(input())
            rocky_x,rocky_y = int(input()),int(input())
            home_x,home_y = int(input()),int(input())

        self.home = Home(home_x,home_y,32,32,IMG_HOME,"home")
        self.flippy = Home(flippy_x,flippy_y,32,32,IMG_HOME,"flippy")
        self.rocky = Home(rocky_x,rocky_y,32,32,IMG_HOME,"rocky")
        stage.add_object(self.home)
        stage.add_object(self.flippy)
        stage.add_object(self.rocky)
        stage.add_object(Road(0,0,flippy_x,flippy_y,5,"yellow"))
        stage.add_object(Road(0,0,rocky_x,rocky_y,5,"yellow"))
        stage.add_object(Road(flippy_x,flippy_y,rocky_x,rocky_y,5,"yellow"))
        stage.add_object(Road(home_x,home_y,flippy_x,flippy_y,5,"yellow"))
        stage.add_object(Road(home_x,home_y,rocky_x,rocky_y,5,"yellow"))
        if INTERACTIVE:
            print(dedent(self.__doc__).strip())
            print(f"Flippy appears at ({self.flippy.x:.2f},{self.flippy.y:.2f})")
            print(f"Rocky appears at ({self.rocky.x:.2f},{self.rocky.y:.2f})")
            print(f"Home appears at ({self.home.x:.2f},{self.home.y:.2f})")
        stage.total_distance = 0
        return stage.turtle,self.home,self.flippy,self.rocky

    def shortest_path(self):
        dist1 = ( distance(0,0,self.flippy.x,self.flippy.y) +
                  distance(self.flippy.x,self.flippy.y,self.rocky.x,self.rocky.y) +
                  distance(self.rocky.x,self.rocky.y,self.home.x,self.home.y) )
        dist2 = ( distance(0,0,self.rocky.x,self.rocky.y) +
                  distance(self.rocky.x,self.rocky.y,self.flippy.x,self.flippy.y) +
                  distance(self.flippy.x,self.flippy.y,self.home.x,self.home.y) )
        return min(dist1,dist2)

    def done(self):
        verify_turtle()
        if INTERACTIVE:
            print("Evaluating...")
        else:
            print("Seed =",13)
        print("Check if Turtle stopped at Flippy's: ", end="")
        if any(self.flippy.contains(stop) for stop in stage.stops):
            print("PASSED")
        else:
            print("FAILED")
        print("Check if Turtle stopped at Rocky's: ", end="")
        if any(self.rocky.contains(stop) for stop in stage.stops):
            print("PASSED")
        else:
            print("FAILED")
        print("Check if Turtle is home: ", end="")
        if self.home.contains(stage.turtle):
            print("PASSED")
            print("Check path being shortest: ", end="")
            if stage.total_distance < self.shortest_path() + 5:
                print("PASSED")
            else:
                print("FAILED")
        else:
            print("FAILED")

    def pos_changed(self,turtle,opos,npos,distance):
        stage.total_distance += distance


# mask everything inside the module except necessary objects
mod = ModuleType(__name__)
sys.modules[__name__] = mod
mod.turtle = stage.turtle
task = Task()
turtle,home,flippy,rocky = task.start()
mod.check = task.done
mod.turtle = turtle
mod.home = home
mod.flippy = flippy
mod.rocky = rocky

if __name__ == "__main__":
    lab_name = os.path.basename(__file__).split(".")[0]
    print("DO NOT RUN THIS FILE DIRECTLY!")
    print("To use this module, run the following command:")
    print()
    objs = ",".join(o for o in dir(mod) if not o.startswith("__"))
    print(f"  from {lab_name} import {objs}")
    print()
    print("Exiting.")
    sys.exit(1)

