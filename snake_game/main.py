from turtle import Screen, Turtle
import time
from snake import snake 
from food import Food
from score import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake1 = snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(.5)
	snake1.move()
	


	if snake1.head.distance(food) < 15:
		print(" nom nom nom")
		food.refresh()
		score.update()
		snake1.extend()
	if abs(snake1.head.xcor() ) > 280	or abs(snake1.head.ycor() ) > 280:
		game_is_on = False
		score.game_over()
	for segment in snake1.segment[1:]:
				
		if snake1.head.distance(segment) < 10:
			game_is_on = False
			score.game_over()		

screen.exitonclick()
