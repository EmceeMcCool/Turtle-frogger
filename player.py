from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def back(self):
        self.setheading(270)
        self.fd(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.7
