from turtle import Turtle, Screen
from random import randint
import time

screen = Screen()
screen.screensize(800,800)
screen.tracer(0)

#Create The Left Paddle
left_paddle = Turtle()
left_paddle.penup()
left_paddle.setpos(-400,0)
left_paddle.setheading(90)
left_paddle.speed(10)
left_paddle.color("blue")
left_paddle.shape("square")
left_paddle.shapesize(0.8, 4)


def move_up():
	left_paddle.setheading(90)
	left_paddle.forward(20)


def move_down():
	left_paddle.setheading(270)
	left_paddle.forward(20)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")


ball = Turtle()
ball.penup()
ball.shape("circle")

game_on = True
while game_on:
	screen.listen()
	# time.sleep(0.1)
	screen.update()



screen.exitonclick()