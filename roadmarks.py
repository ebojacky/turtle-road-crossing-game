from turtle import Turtle

MARGIN = 40
LANE_SIZE = 30
BROKEN_LINE_FACTOR = 10


class RoadMark(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")

        self.w = self.getscreen().window_width()
        self.h = self.getscreen().window_height()
        self.down_border = [(-self.w / 2, -self.h / 2 + MARGIN), (self.w / 2, -self.h / 2 + MARGIN)]
        self.no_of_lanes = int((self.h - 2 * MARGIN) / LANE_SIZE)

        self.draw_lanes()

    def draw_solid(self, xy_start, xy_end):
        self.penup()
        self.goto(xy_start)
        self.pendown()
        self.goto(xy_end)

    def draw_broken(self, xy_start, xy_end):
        self.penup()
        self.goto(xy_start)
        self.setheading(0)

        for _ in range(int(xy_start[0]), int(xy_end[0]), BROKEN_LINE_FACTOR):
            self.pendown()
            self.forward(BROKEN_LINE_FACTOR)
            self.penup()
            self.forward(BROKEN_LINE_FACTOR)

    def draw_lanes(self):
        for i in range(0, self.no_of_lanes + 1):
            if i in [0, self.no_of_lanes]:
                self.draw_solid((self.down_border[0][0], self.down_border[0][1] + i * LANE_SIZE),
                                (self.down_border[1][0], self.down_border[1][1] + i * LANE_SIZE))

            else:
                self.draw_broken((self.down_border[0][0], self.down_border[0][1] + i * LANE_SIZE),
                                 (self.down_border[1][0], self.down_border[1][1] + i * LANE_SIZE))
