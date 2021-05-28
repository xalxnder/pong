from turtle import Turtle, Screen
from random import randint
import time
screen = Screen()
screen.screensize(600, 600)
screen.setup(900,700)
screen.tracer(0)

#Create The Players Paddle
player_paddle = Turtle()
player_paddle.penup()
player_paddle.setpos(-400,0)
player_paddle.setheading(90)
player_paddle.speed(10)
player_paddle.color("blue")
player_paddle.shape("square")
player_paddle.shapesize(0.8, 4)


#Create the Computers Paddle
cpu_paddle = Turtle()
cpu_paddle.penup()
cpu_paddle.setpos(400,0)
cpu_paddle.setheading(90)
cpu_paddle.speed(10)
cpu_paddle.color("blue")
cpu_paddle.shape("square")
cpu_paddle.shapesize(0.8, 4)


def move_up():
	if player_paddle.ycor() < 400:
		player_paddle.setheading(90)
		player_paddle.forward(20)


def move_down():
	if player_paddle.ycor() > -400:
		player_paddle.setheading(270)
		player_paddle.forward(20)


def cpu_move():
	cpu_paddle.forward(20)
	if cpu_paddle.ycor() == 300:
		cpu_paddle.setheading(270)
	elif cpu_paddle.ycor() == -300:
		cpu_paddle.setheading(90)



screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

ball = Turtle()
ball.penup()
ball.shape("circle")
ball.speed(5)
ball.dx = 15
ball.dy = 15

print(player_paddle.pos())
game_on = True

while game_on:
	screen.update()
	cpu_move()
	ball.sety(ball.ycor() + ball.dy)
	ball.setx(ball.xcor() + ball.dx)
	if ball.ycor() > 300:
		ball.dx *= -1
		ball.dy *= -1
	if ball.ycor() < -300:
		ball.dx *= -1
		ball.dy *= -1
	if ball.distance(player_paddle) < 15:
		ball.dx *= -1
		ball.dy *= -1

	screen.listen()
	time.sleep(0.1)


screen.exitonclick()