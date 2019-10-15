#Kathryn Marini 10/15/19
import turtle
bob = turtle.Turtle()

turtle.hideturtle()

#This creates a 5 pointed gold star. 
bob.color('gold')
bob.begin_fill()
for x in range(0,5):
	bob.showturtle()
	bob.forward(150)
	bob.right(144)
	bob.hideturtle()
bob.end_fill()	
