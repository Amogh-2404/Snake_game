import turtle
from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
board = Scoreboard()


#Creates snake
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


screen.update()

#Moves snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
#range function is not pure python and comes from the C language and does not let us pass the values to the functions using names.
    snake.move()

#detect collsion with food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       board.refresh()
#detect collision with wall
    if snake.head.xcor() > 300 or snake.head.ycor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() < -280:
       game_is_on = False
       board.game_over()

#detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            board.game_over()


screen.exitonclick()