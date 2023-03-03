"""Creates Player class for Turtle Crossing"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
TEAL = "#34ACAD"
WHITE = "#ECE3C9"

class Player(Turtle):
    """Player class (player is a turtle)"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(TEAL)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Makes the turtle move up"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Makes the turtle move down"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        """Makes the turtle move left"""
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        """Makes the turtle move right"""
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def restart(self):
        """Resets the turtle to the starting position"""
        self.goto(STARTING_POSITION)
