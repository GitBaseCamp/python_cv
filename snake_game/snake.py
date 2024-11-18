import time
from turtle import Turtle,Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0) ]
MOVE_DISTANCE =  20

UP=90
DOWN=270
LEFT=180
RIGHT=0

#tarting_positions = [(0,0),(-20,0),(-40,0) ]
#egment = []


class snake:
	def __init__(self):
				
		self.segment=[]
		self.create_snake()
		self.head = self.segment[0]
#	screen = Screen()
	def  create_snake(self):
		for position in STARTING_POSITION:
			self.add_segment(position)
			
	def add_segment(self, position):
		new_segment = Turtle("square")
		new_segment.color("white")
		new_segment.penup()
		new_segment.goto(position)
		self.segment.append(new_segment)

	def extend(self):
		self.add_segment(self.segment[-1].position())
		
	def move(self):
			
		for seg_num in range(len(self.segment) - 1,0,-1):
			new_x = self.segment[seg_num -1].xcor()
			new_y = self.segment[seg_num -1].ycor()
			self.segment[seg_num].goto(new_x, new_y)
		self.segment[0].forward(MOVE_DISTANCE)
#			self.segment[0].left(90)
	def up(self):
		if self.head.heading() != DOWN:
			self.segment[0].setheading(90)
	def right(self):
		if self.head.heading() != LEFT:
			self.segment[0].setheading(0)
	def left(self):
		if self.head.heading() != RIGHT:
			self.segment[0].setheading(180)
	def down(self):
		if self.head.heading() != UP:
			self.segment[0].setheading(270)	
##	screen.exitonclick()

