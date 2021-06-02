from turtle import Turtle, Screen
from random import randint
import time
screen = Screen()
screen.screensize(600, 600)
screen.setup(900,700)
screen.tracer(0)

#Create The Players Paddle
left_paddle = Turtle()
left_paddle.penup()
left_paddle.setpos(-400,0)
left_paddle.setheading(90)
left_paddle.speed(0)
left_paddle.color("blue")
left_paddle.shape("square")
left_paddle.shapesize(0.8, 4)

#Create The Players Paddle
right_paddle = Turtle()
right_paddle.penup()
right_paddle.setpos(400,0)
right_paddle.setheading(90)
right_paddle.speed(0)
right_paddle.color("blue")
right_paddle.shape("square")
right_paddle.shapesize(0.8, 4)



ball = Turtle()
ball.penup()
ball.shape("circle")
ball.speed(8)

def left_move_up():
	if left_paddle.ycor() < 290:
		left_paddle.setheading(90)
		left_paddle.forward(20)


def left_move_down():
	if left_paddle.ycor() > -290:
		left_paddle.setheading(270)
		left_paddle.forward(20)


def right_move_up():
	if right_paddle.ycor() < 290:
		right_paddle.setheading(90)
		right_paddle.forward(20)


def right_move_down():
	if right_paddle.ycor() > -290:
		right_paddle.setheading(270)
		right_paddle.forward(20)



ball_x_move = -10
ball_y_move = -10


def move_ball():
	ball.goto((ball.xcor() + ball_x_move), (ball.ycor() + ball_y_move))


screen.listen()
#Player 1


#Player 2
screen.onkey(right_move_up, "Up")
screen.onkey(right_move_down, "Down")
screen.onkey(left_move_up, "w")
screen.onkey(left_move_down, "s")

game_on = True

while game_on:
	screen.delay(30)
	screen.update()
	move_ball()
	if ball.ycor() >= 330 or ball.ycor() <= -330:
		ball_y_move *= -1

	if ball.distance(left_paddle) < 50:
		ball_x_move *= -1
		print("ouch")

	if ball.distance(right_paddle) < 50:
		ball_x_move *= -1
		print("ouch")


	time.sleep(0.1)


screen.exitonclick()