import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.back, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_is_on = True
times_gone = 0
cars = []
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    if times_gone % 6 == 0:
        cars.append(CarManager())
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        if player.ycor() >= FINISH_LINE_Y:
            player.reset()
            scoreboard.new_level()

    times_gone += 1


screen.exitonclick()



