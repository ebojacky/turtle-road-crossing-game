from turtle import Turtle

SCORE_MARGIN = 30
FONT = ("Arial", 16, "normal")
TIME_TO_CROSS = 30


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.level = 1
        self.score = 0
        self.timer = TIME_TO_CROSS
        self.goto(0, (self.getscreen().window_height() / 2 - SCORE_MARGIN))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Time:{self.timer}  Level:{self.level}  Score:{self.score}", font=FONT, align='center')

    def update_score(self):
        self.score += (self.level - 1) + self.timer
        self.refresh()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def update_timer(self):
        self.timer -= 1

    def reset_timer(self):
        self.timer = TIME_TO_CROSS
        self.refresh()
