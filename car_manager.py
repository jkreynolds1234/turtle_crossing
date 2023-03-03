"""Car manager and Car classes for Turtle Crossing"""
from turtle import Turtle
import random
import time

BGCOLOR = "#22201A"

PINK = "#AF3A8A"
SALMON = "#C45A6F"
ORANGE = "#BF6C1F"
YELLOW = "#BD8D1A"
PURPLE = "#904491"
BURGUNDY = "#752D41"
INDIGO = "#5F4CA2"

COLORS = [PINK, SALMON, ORANGE, YELLOW, PURPLE, BURGUNDY, INDIGO]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7
NUM_CARS = 5
CREATION_DECREMENT = 2

class CarManager():
    """Car Manager Class for Turtle Crossing game"""
    def __init__(self):
        self.cars = []
        self.cars.append(Car())
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_creation = 6

    def create_car(self):
        """Creates a car"""
        random_chance = random.randint(1, self.car_creation)
        if random_chance == 1 or ((time.time() - self.cars[-1].created_at) > 2):
            new_car = Car()
            # Prevents cars of the same color from being created within 2 car creations of each other
            if len(self.cars) == 1:
                color_list = [color for color in COLORS if color != self.cars[-1].car_color]
                new_car.car_color = random.choice(color_list)
                new_car.color(new_car.car_color)
                # Prevents cars being created at the same y coordinate twice in a row
                y_list_range = [number for number in range(-200, 240, 20) if number != self.cars[-1].ycor()]
                new_y = random.choice(y_list_range)
                new_car.goto(new_car.xcor(), new_y)

            else:
                color_list = [color for color in COLORS if color not in [self.cars[-1].car_color, self.cars[-2].car_color]]
                new_car.car_color = random.choice(color_list)
                new_car.color(new_car.car_color)
                y_list_range = [number for number in range(-200, 240, 20) if number not in [self.cars[-1].ycor(), self.cars[-2].ycor()]]
                new_y = random.choice(y_list_range)
                new_car.goto(new_car.xcor(), new_y)
            self.cars.append(new_car)

    def move_cars(self):
        """Moves cars left"""
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase car speed with each level"""
        self.car_speed += MOVE_INCREMENT

class Car(Turtle):
    """Car class for Turtle Crossing game"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.car_color = random.choice(COLORS)
        self.color(self.car_color)
        self.penup()
        random_y = random.randrange(-220, 240, 20)
        self.goto(300, random_y)
        self.passed = False
        self.created_at = time.time()
