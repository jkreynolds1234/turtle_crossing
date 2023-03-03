"""Scoreboard Class for Turtle Crossing"""
from turtle import Turtle

X_LARGE_FONT = ("Courier", 36, "bold")
LARGE_FONT = ("Courier", 26, "bold")
FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"
WHITE = "#ECE3C9"
ORANGE = "#E3802A"
TEAL = "#2DC2C7"
STARTING_POSITION = -280

class Scoreboard(Turtle):
    """Scoreboard Class"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.level = 1
        self.color(WHITE)
        self.goto(0, 155)
        self.write("TURTLE", align=ALIGNMENT, font=X_LARGE_FONT)
        self.goto(0, 95)
        self.write("CROSSING", align=ALIGNMENT, font=X_LARGE_FONT)
        self.color(ORANGE)
        self.goto(0, 30)
        self.write('Use the arrow keys to move.', align=ALIGNMENT, font=FONT)
        self.goto(0, -25)
        self.color(TEAL)
        self.write('Get to the other side,', align=ALIGNMENT, font=FONT)
        self.goto(0, -60)
        self.write('without being hit!', align=ALIGNMENT, font=FONT)
        self.color(WHITE)
        self.goto(0, -140)
        self.write('Press "g" to start', align=ALIGNMENT, font=LARGE_FONT)

    def update_score(self):
        """Updates the score"""
        self.color(WHITE)
        if self.score >= 100:
            self.goto(195, 255)
        elif self.score >= 10:
            self.goto(205, 255)
        elif self.score < 10:
            self.goto(215, 255)
        self.write("SCORE: {}".format(round(self.score)), align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Updates the Scoreboard"""
        self.clear()
        self.color(WHITE)
        self.goto(0, 250)
        self.write("LEVEL {}".format(self.level), align=ALIGNMENT, font=LARGE_FONT)
        self.goto(-220, 255)
        self.write("LIVES: {}".format(self.lives), align=ALIGNMENT, font=FONT)
        self.update_score()

    def lose_life(self):
        """Makes the player lose a life"""
        self.lives -= 1
        self.update_scoreboard()

    def increase_score(self, player_ycor):
        """Increase the player's score for each car passed depending on how far they have moved across the screen"""
        if player_ycor > STARTING_POSITION:
            self.score += .75 * (player_ycor - STARTING_POSITION)/530
            self.update_scoreboard()

    def game_over(self):
        """Write Game Over message on the screen"""
        self.clear()
        self.color(WHITE)
        self.goto(0, 100)
        self.write("GAME", align=ALIGNMENT, font=X_LARGE_FONT)
        self.goto(0, 30)
        self.write("OVER", align=ALIGNMENT, font=X_LARGE_FONT)
        self.goto(0, -30)
        self.write("FINAL SCORE: {}".format(round(self.score)), align=ALIGNMENT, font=LARGE_FONT)

    def win(self):
        """Writes You Win message on the screen"""
        self.clear()
        self.color(WHITE)
        self.goto(0, 100)
        self.write("YOU", align=ALIGNMENT, font=X_LARGE_FONT)
        self.goto(0, 30)
        self.write("WIN", align=ALIGNMENT, font=X_LARGE_FONT)
        self.goto(0, -30)
        self.write("FINAL SCORE: {}".format(round(self.score)), align=ALIGNMENT, font=LARGE_FONT)

    def level_welcome(self):
        """Welcome screen for the levels"""
        self.clear()
        self.color(WHITE)
        self.goto(0, 0)
        self.write("LEVEL {} ".format(self.level), align=ALIGNMENT, font=X_LARGE_FONT)
