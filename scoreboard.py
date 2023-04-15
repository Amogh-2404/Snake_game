from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.points = 0
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score:{self.points}", move=False,align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def refresh(self):
        self.clear()
        self.points = self.points + 1
        self.pendown()
        self.write(f"Score:{self.points}", move=False,align=ALIGNMENT, font=FONT)
        self.penup()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(f"GAME OVER", move=False,align=ALIGNMENT, font=FONT)


