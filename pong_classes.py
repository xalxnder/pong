import turtle
from turtle import Turtle, Screen


class LeftPaddle(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.setpos(-400, 0)
		self.setheading(90)
		self.speed(0)
		self.color(61, 84, 103)
		self.shape("square")
		self.shapesize(0.8, 4)
		self.score = 0

	def up(self):
		if self.ycor() < 290:
			self.setheading(90)
			self.forward(20)

	def down(self):
		if self.ycor() > -290:
			self.setheading(270)
			self.forward(20)


class RightPaddle(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.setpos(400, 0)
		self.setheading(90)
		self.speed(0)
		self.color(61, 84, 103)
		self.shape("square")
		self.shapesize(0.8, 4)
		self.score=0

	def up(self):
		if self.ycor() < 290:
			self.setheading(90)
			self.forward(20)

	def down(self):
		if self.ycor() > -290:
			self.setheading(270)
			self.forward(20)


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("circle")
		self.speed(8)
		self.dx = 10
		self.dy = 10

	def move(self):
		self.goto((self.xcor() + self.dx), (self.ycor() + self.dy))

	def reset(self):
		self.goto(0, 0)


class ScoreBoard(Turtle):
	def __init__(self, player, score, cord):
		super().__init__()
		self.player = player
		self.cord = cord
		self.score = score
		self.penup()
		self.hideturtle()
		self.goto(cord)
		self.color(219, 84, 97)
		self.write(f"{self.player}: {self.score}", True, align="center", font=("Arial", 30, "normal"))


class HalfCourt(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.setheading(90)
		self.color(138, 162, 158)
		self.shape("square")
		self.shapesize(0.5, 1)
