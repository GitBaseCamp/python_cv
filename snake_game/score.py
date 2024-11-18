from turtle import Turtle, Screen

#screen = Screen()

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.writ()
	def writ(self):	
		self.color("white")
		self.penup()
		self.goto(0,270)
		self.write(f"socre:{self.score}", align="center", font=("Arial", 24, "normal") )
		self.hideturtle()
		
	def update(self):
		self.clear()
		self.score +=1 
		self.write(f"socre:{self.score}", align="center", font=("Arial", 24, "normal") )
			
	def game_over(self):
		self.color("white")
		self.penup()
		self.goto(0,0)
		self.write(f"Game Over!", align="center", font=("Arial", 24, "normal") )
		self.hideturtle()
	
#Score()
#screen.exitonclick()

