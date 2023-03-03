"""Turtle Crossing Game"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

BGCOLOR = "#22201A"
FINISH_LINE = 245

screen = Screen()

class TurtleCrossing():
    """Class for Turtle Crossing Game"""
    def __init__(self):
        self.game_is_on = False
        self.screen = Screen()
        self.screen.bgcolor(BGCOLOR)
        self. screen.setup(width=600, height=600)
        self.screen.title("Turtle Crossing")
        # Turns off animation, manually updated in while loop below
        self.screen.tracer(0)

        # Welcome message
        self.scoreboard = Scoreboard()

        # Listen for key presses
        self.screen.listen()
        self.screen.onkey(self.level_one_start, "g")
        self.screen.exitonclick()

    def level_one_start(self):
        """Shows Level 1 Welcome screen and then starts the game"""
        self.scoreboard.level_welcome()
        time.sleep(2)
        self.start_game()

    def start_game(self):
        """Starts the game"""
        self.game_is_on = True
        self.player = Player()
        self.car_manager = CarManager()

        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

        while self.game_is_on:
            time.sleep(0.1)
            self.screen.update()
            self.car_manager.create_car()
            self.car_manager.move_cars()
            self.scoreboard.update_scoreboard()

            # Detect if car hits turtle
            for car in self.car_manager.cars:
                if self.player.xcor() > (car.xcor() - 27) and self.player.xcor() < (car.xcor() + 27):
                    if self.player.ycor() > (car.ycor() - 21) and self.player.ycor() < (car.ycor() + 21):
                        self.scoreboard.lose_life()
                        if self.scoreboard.lives > 0:
                            self.game_is_on = False
                            time.sleep(.25)
                            self.player.restart()
                            self.game_is_on = True
                        else:
                            self.game_is_on = False
                            self.scoreboard.game_over()

                # Detect how many cars have passed
                if car.xcor() < -63 and not car.passed:
                    car.passed = True
                    # Manage increase in score
                    self.scoreboard.increase_score(self.player.ycor())

            # Detect if player has made it to the other side
            if self.player.ycor() > FINISH_LINE:
                self.game_is_on = False
                self.scoreboard.level += 1
                if self.scoreboard.level <= 4:
                    self.scoreboard.level_welcome()
                    if self.scoreboard.level == 2:
                        self.car_manager.car_creation = 4
                    elif self.scoreboard.level == 3:
                        self.car_manager.car_creation = 3
                    elif self.scoreboard.level == 4:
                        self.car_manager.car_creation = 2
                    time.sleep(2)
                    self.player.restart()
                    self.car_manager.level_up()
                    self.game_is_on = True
                else:
                    self.scoreboard.win()

game = TurtleCrossing()
