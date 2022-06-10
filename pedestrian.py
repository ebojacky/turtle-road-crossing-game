from turtle import Turtle

X_MARGIN = 20
Y_MARGIN = 20
ONE_STEP = 20


class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.start_position()

    def start_position(self):
        self.goto(-self.getscreen().window_width() / 4, -self.getscreen().window_height() / 2 + Y_MARGIN)

    def move_up(self):
        self.forward(ONE_STEP)

    def move_down(self):
        self.forward(-ONE_STEP)

    def at_finish_line(self):
        return abs(self.ycor()) >= self.getscreen().window_height() / 2
