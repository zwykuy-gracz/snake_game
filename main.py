from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.end_of_game()
        game_is_on = False

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.end_of_game()

    screen.onkeypress(snake.turn_left, 'a')
    screen.onkeypress(snake.turn_right, 'd')


screen.exitonclick()