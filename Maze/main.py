import time

import turtle


turtle.register_shape("Player5.gif")
turtle.register_shape("Block4.gif")
turtle.register_shape("Door2.gif")
turtle.register_shape("Player4.gif")

""" ****************************************    MODEL   *************************************************************
 ************************                                                      **********************************"""

class Model(turtle.Turtle):


    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Player5.gif")

        self.penup()
        self.speed(0)

    cost = 0
    # in goal punem starea de goal
    goal = []
    trace = []

    path = []
    init_state = []
    visited = set()
    #frontier = deque
    solution = {}

    walls = []

        # Create levels list
    levels = [""]  # lista de niveluri

        # Define first Level
    level_1 = [
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XX          XXXXXXXXX  XX",
        "XXXXXXX  XXXXXXXXXXXX  XX",
        "XXXXXXX  XXXXXXXXXXXXXXXX",
        "XXXXXXX      XXXXXXXXXXXX",
        "XX      XXXX   XXXXXXXXXX",
        "XXXXXXX XXXXX  XXXXXXXXXX",
        "XXXXXXX XXXXXX XXXXXXXXXX",
        "XX          XXXXXXXXXXXXX",
        "XXXXXXXXXX      XXXXXXXXX",
        "XXXXX  XXX    XXXXXXXXXXX",
        "XXXXXXXXXX    XXXXXXXXXXX",
        "X           SP          X",
        "XXXXXXXXXXXXXXXXXX     XX",
        "XXXXXXXXXX  XXXX     XXXX",
        "XX   XXXXX  XXXXX   XXXXX",
        "XX   XXXX           XXXXX",
        "XX   XXXX      X   XXXXXX",
        "XXXXXXXXXXXXXXXX   XXXXXX",
        "XXXXXXXXXXXXXX    XXXXXXX",
        "XXXXXXXXXXXXX  XX   XXXXX",
        "XXXXXXXXXXX   XXXX   XXXX",
        "XXXXXXXXX   XXXXXXXX  XXX",
        "XXXXXXXXX   XXXXXXXXX   G",
        "XXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
    levels.append(level_1)
    wn = turtle.Screen()


  

    def go_down(self):


        move_x = self.xcor()
        move_y = self.ycor() - 24
        self.shape("square")
        self.color("green")
        self.stamp()
        if (move_x, move_y) not in Model.walls:
            self.goto(move_x, move_y)
            self.shape("Player5.gif")
        if (move_x, move_y) in Model.goal:

            Model.wn.bye()

    def go_right(self):


        move_x = self.xcor() + 24
        move_y = self.ycor()
        self.shape("square")
        self.color("green")
        self.stamp()

        if (move_x, move_y) not in Model.walls:
            self.goto(move_x, move_y)
            self.shape("Player5.gif")

        if (move_x, move_y) in Model.goal:

            Model.wn.bye()


    def go_left(self):


        move_x = self.xcor() - 24
        move_y = self.ycor()
        self.shape("square")
        self.color("green")
        self.stamp()

        if (move_x, move_y) not in Model.walls:
            self.goto(move_x, move_y)
            self.shape("Player4.gif")

        if (move_x, move_y) in Model.goal:
            Model.wn.bye()


    def go_up(self):

        move_x = self.xcor()
        move_y = self.ycor() + 24
        self.shape("square")
        self.color("green")
        self.stamp()

        if (move_x, move_y)  not in Model.walls:
            self.goto(move_x, move_y)
            self.shape("Player5.gif")

        if (move_x, move_y) in Model.goal:

            Model.wn.bye()

""" ****************************************    PRESENTER   *************************************************************
 ************************                                                      **********************************"""

class Presenter(turtle.Turtle):  # DESENAM MAZE UL IN TIMP REAL, Clasa Pen este copil a clasei Turtle din mdodulul turtle,clasa defineste un obiect
    def __init__(self):# refera obiectul
        turtle.Turtle.__init__(self)  # initializam clasa Turtle deoarece folosim Pen care este copil al ei
        self.shape("square")
        self.color("black")
        self.penup()  # Pen is up
        self.speed(0)  # viteza animatiei, 0 is the fastest


    def setup_maze(self,level):

        global start_x,start_y
        global end_x,end_y

        for y in range(len(level)):
            for x in range(len(level[y])):
                # acceseaza caracterul de la pozitia x,y

                character = level[y][x]

                # Calculam coordonatele astfel incsat sa se potriveasca cu marimea eranului
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "P":
                    player.goto(screen_x, screen_y)
                    start_x=screen_x
                    start_y=screen_y
                    # player.shape("Player5.gif")

                if character == "G":
                    door.goto(screen_x, screen_y)
                    door.shape("Door2.gif")
                    door.stamp()
                    Model.goal.append((screen_x, screen_y))

                # daca caracterul este un x il punem pe ecran
                if character == "X":
                    grid.goto(screen_x, screen_y)
                    grid.shape("Block4.gif")
                    grid.stamp()  # pune pe ecran,si ramana in pozitia respectiva (don t move)
                    # Adaugam blocurile (tupla x,y)) in lista de pereti
                    Model.walls.append((screen_x, screen_y))
                    

    def listen(self):
        turtle.listen()

        # turtle.onclick()
        turtle.onkey(player.go_left, "Left")  # player numele instantei, go left numele metodei, Left - left arrow
        turtle.onkey(player.go_right, "Right")
        turtle.onkey(player.go_up, "Up")
        turtle.onkey(player.go_down, "Down")

    def init_window(self):

        Model.wn.bgcolor("black")
        Model.wn.title("MazeGameAi")
        Model.wn.setup(700, 700)

grid=Presenter()
player=Model()
door=Presenter()


""" ****************************************    VIEW   *************************************************************
 ************************                                                      **********************************"""


class View():

    def setup_game(self):


        Presenter.init_window(grid)
        Presenter.setup_maze(grid,Model.level_1)
        Presenter.listen(grid)


view = View()

def main():


    View.setup_game(view)

    while True:

        Model.wn.update()


if __name__ == "__main__":
    main()
