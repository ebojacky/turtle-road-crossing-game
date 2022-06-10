import random
import turtle
from turtle import Turtle
from random import randint, choice

SIZE_OPTIONS = [(1, 1), (1, 2)]
X_MARGIN = 20
Y_MARGIN = 60
INITIAL_STEP = 5
SPECIAL_STEP = 3
LANE_SIZE = 30
CAR_POSITION_ADJUSTMENT = -5

turtle.colormode(255)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_flag = random.choice(["slow", "normal", "fast"])


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.size_options = SIZE_OPTIONS
        self.hideturtle()
        self.lanes = range(int(-(self.getscreen().window_height() / 2 - Y_MARGIN - CAR_POSITION_ADJUSTMENT)),
                           int((self.getscreen().window_height() / 2 - Y_MARGIN - CAR_POSITION_ADJUSTMENT)), LANE_SIZE)
        self.all_cars = []
        self.step = INITIAL_STEP

    def create_car(self, game_level=1):
        number_of_cars_to_create = int(game_level / 2)
        if number_of_cars_to_create < 1:
            number_of_cars_to_create = 1
        for i in range(0, number_of_cars_to_create):
            new_car = Car()
            new_car.shape("square")
            car_size = random.choice(self.size_options)
            new_car.shapesize(car_size[0], car_size[1])
            new_car.penup()
            new_car.setheading(180)

            new_car.color(randint(0, 255), randint(0, 255), randint(0, 255))

            x = new_car.getscreen().window_width() / 2 - X_MARGIN
            y = random.choice(self.lanes)
            new_car.goto(x, y)

            self.all_cars.append(new_car)

    def move(self, activate_different_speeds=False):
        if not activate_different_speeds:
            for car in self.all_cars:
                car.forward(self.step)
                self.remove_off_screen_car(car)
        else:
            for car in self.all_cars:
                if car.speed_flag == "slow":
                    car.forward(self.step - SPECIAL_STEP)
                elif car.speed_flag == "normal":
                    car.forward(self.step)
                elif car.speed_flag == "fast":
                    car.forward(self.step + SPECIAL_STEP)

                # delete cars that have moved off-screen
                self.remove_off_screen_car(car)

    def remove_off_screen_car(self, car):
        if car.xcor() < - (self.getscreen().window_width() + 5 * X_MARGIN) / 2:
            car.hideturtle()
            self.all_cars.remove(car)

    def increase_speed(self):
        self.step += 1
