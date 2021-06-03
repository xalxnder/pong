import turtle
from turtle import Screen
from pong_classes import *
import time

#Main Setup
turtle.colormode(255)
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor(241, 237, 238)
screen.setup(900, 700)
screen.tracer(0)
left_paddle = LeftPaddle()
right_paddle = RightPaddle()
ball = Ball()
player_1_scoreboard = ScoreBoard(player="Player 1", cord=(-250, 290), score=left_paddle.score)
player_2_scoreboard = ScoreBoard(player="Player 2", cord=(250, 290), score=right_paddle.score)


#Half Court
init_pos = -320
for i in range(16):
	half_court = HalfCourt()
	half_court.setpos(0, init_pos)
	init_pos += 50


#Player Controls
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True

while game_on:
	screen.update()
	ball.move()
	if ball.ycor() >= 330 or ball.ycor() <= -330:
		ball.dy *= -1

	if ball.distance(left_paddle) < 50:
		ball.dx *= -1

	if ball.distance(right_paddle) < 50:
		ball.dx *= -1

	if ball.xcor() >= 440:
		ball.reset()
		player_1_scoreboard.clear()
		left_paddle.score += 1
		player_1_scoreboard = ScoreBoard(player="Player 1", cord=(-250, 290), score=left_paddle.score)

	if ball.xcor() <= -440:
		ball.reset()
		player_2_scoreboard.clear()
		left_paddle.score += 1
		player_2_scoreboard = ScoreBoard(player="Player 2", cord=(250, 290), score=right_paddle.score)
	time.sleep(0.1)

screen.exitonclick()
