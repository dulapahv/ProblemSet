import turtle

def RobotBattle():
    #robotList stores the list of robots in the battle 
    robotList = [];

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()       

        #Display the status of each robot
        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(i, " : ",)
            robot.displayStatus()            
            i+=1        
        print("===============")

        #Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot")               
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
        i=0
        for robot in robotList:
            if(robot.health <=0):
                del robotList[i]
            i+=1


class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100
                                  
    def move(self,x,y):
    # Your code
        pass
    
    def draw(self):
    # Your code
        pass

    def displayStatus(self):
        print("x=", self.x, "y=", self.y, "health=", self.health, "energy=", self.energy)
                                  
    def command(self, robotList):
        print("Possible actions: move")    
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX,newY)            


class MedicBot(Robot):       
    # Your code
        pass


class StrikerBot(Robot): 
    # Your code
        pass
