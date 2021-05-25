from turtle import Turtle, Screen
from random import randint
import time

screen = Screen()
screen.screensize(800,800)
screen.tracer(0)
left_paddle = []
right_paddle = []
left_count = 0
right_count = 0




#Create The Left Paddle
for i in range(4):
	paddle = Turtle()
	paddle.penup()
	paddle.shape("square")
	left_paddle.append(paddle)
	paddle.setpos(-400, left_count)
	left_count += 15

#Create The Right Paddle
for i in range(4):
	paddle = Turtle()
	paddle.penup()
	paddle.shape("square")
	left_paddle.append(paddle)
	paddle.setpos(400,right_count)
	right_count += 15


ball = Turtle()
ball.shape("circle")
screen.listen()
time.sleep(0.1)
screen.update()



screen.exitonclick()