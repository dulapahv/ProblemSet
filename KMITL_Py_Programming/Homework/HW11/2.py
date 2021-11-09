import turtle
turtle.speed(0)
turtle.ht()

def RobotBattle():
    #robotList stores the list of robots in the battle
    robotList = []

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
        
        #Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")
            
        #Ask user which robot to command or to create a new robot
        choice = input("Enter which type of robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for Medicbot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        #Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1


class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10

    def draw(self):
        turtle.pu()
        turtle.setpos(self.x, self.y)
        turtle.rt(90)
        turtle.fd(15)
        turtle.lt(90)
        turtle.pd()
        turtle.circle(15)

    def displayStatus(self):
        print(f"x = {self.x} y = {self.y}")
        print(f"Health = {self.health} Energy = {self.energy}")

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)


class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        if self.energy >= 20 and self.x - r.x <= 10 and self.y - r.y <= 10:
            r.health += 10
            self.energy -= 20
        elif self.energy < 20:
            print("Not enough energy!")
        elif self.x - r.x <= 10 and self.y - r.y <= 10:
            print("Chosen robot is too far away!")

    def command(self, robotList):
        print("Possible actions: move, heal")
        cmd = str(input("Choose the command Move(m) or Heal(h): "))
        if cmd == "m":
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)

        elif cmd == "h":
            robot = int(input("Which robot to heal ?: "))
            self.heal(robotList[robot])

    def draw(self):
        super().draw()
        turtle.pencolor("red")
        turtle.pensize(4)
        turtle.lt(90)
        turtle.fd(30)
        turtle.bk(15)
        turtle.rt(90)
        turtle.bk(15)
        turtle.fd(30)
        turtle.pencolor("black")
        turtle.pensize(1)


class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and self.x - r.x <= 10 and self.y - r.y <= 10:
            r.health -= 50
            self.missile -= 1
            self.energy -= 20
        elif self.missile <= 0:
            print("Run out of missiles!")
        elif self.energy < 20:
            print("Not enough energy!")
        elif self.x - r.x <= 10 and self.y - r.y <= 10:
            print("Chosen robot is too far away!")

    def displayStatus(self):
        print("x = %d y = %d" % (self.x, self.y))
        print("Health = %d Energy = %d" % (self.health, self.energy))
        print("Missile = %d" %self.missile)

    def command(self, robotList):
        print("Possible actions: move, attack")
        cmd = input("Choose the command: Move(m) or Strike(s): ")
        if cmd == 'm':
            newx = int(input("Enter new X coordinate: "))
            newy = int(input("Enter new Y coordinate: "))
            self.move(newx, newy)
        elif cmd == 's':
            robot = int(input("Which robot to strike?: "))
            self.strike(robotList[robot])

    def draw(self):
        super().draw()
        turtle.pu()
        turtle.pencolor("blue")
        turtle.lt(90)
        turtle.fd(7)
        turtle.pd()
        turtle.rt(90)
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(8, 360, 4)
        turtle.end_fill()
        turtle.pencolor("black")


RobotBattle()