import time
from turtle import Screen
import threading
import score
from cars import Cars
from pedestrian import Pedestrian
from roadmarks import RoadMark
from score import ScoreBoard

WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = "white"
SCREEN_TITLE = "TURTLE HIGHWAY CROSSING"
TURTLE_CAR_COLLISION_MARGIN = 20
CAR_ADDITION_INTERVAL = 10
SCREEN_REFRESH = 0.1
LEVEL_OF_DIFFERENT_SPEED_PER_CAR = 5

STOP_TIMER_THREAD = False


def play_game():
    screen = Screen()
    screen.bgcolor(SCREEN_COLOR)
    screen.title(SCREEN_TITLE)
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.colormode(255)
    global STOP_TIMER_THREAD
    STOP_TIMER_THREAD = False

    RoadMark()

    my_score = ScoreBoard()
    my_turtle = Pedestrian()
    my_cars = Cars()

    def timer():
        while True:
            global STOP_TIMER_THREAD
            if not STOP_TIMER_THREAD:
                time.sleep(1)
                my_score.update_timer()
            else:
                break

    thread_for_timer = threading.Thread(target=timer)
    thread_for_timer.start()

    screen.listen()
    screen.onkey(my_turtle.move_up, "Up")
    screen.onkey(my_turtle.move_down, "Down")

    game_on = True
    car_addition = CAR_ADDITION_INTERVAL
    while game_on:
        time.sleep(SCREEN_REFRESH)

        if car_addition <= 0:
            my_cars.create_car(my_score.level)
            car_addition = CAR_ADDITION_INTERVAL
        car_addition -= 1

        if my_score.level > LEVEL_OF_DIFFERENT_SPEED_PER_CAR:
            my_cars.move(activate_different_speeds=True)
        else:
            my_cars.move()

        screen.update()

        for car in my_cars.all_cars:
            if my_turtle.distance(car) <= TURTLE_CAR_COLLISION_MARGIN:
                game_on = False

        if my_score.timer in range(1, score.TIME_TO_CROSS):
            my_score.refresh()

        if my_score.timer == 0:
            game_on = False

        if my_turtle.at_finish_line():
            my_score.increase_level()
            my_score.reset_timer()

            my_cars.increase_speed()
            my_turtle.start_position()

    repeat = "N"
    repeat = screen.textinput("Game Over!", "Press Y to play again. N to quit")
    if repeat.upper() == "Y":
        screen.clear()
        STOP_TIMER_THREAD = True
        thread_for_timer.join()
        play_game()

    screen.exitonclick()


play_game()
