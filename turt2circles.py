#Kathryn Marini 10/11/19
import turtle
bob = turtle.Turtle()

#This moves the turtle to the left for the position of the first circle. 
turtle.hideturtle()
bob.hideturtle()
bob.penup()
bob.backward(250)

#This creates the first circle, which is the color lemon chiffon. 
bob.color('lemonchiffon')
bob.begin_fill()
bob.circle(50)
bob.end_fill()

#Second circle, coral. 
bob.forward(125)
bob.color('coral')
bob.begin_fill()
bob.circle(50)
bob.end_fill()

#Third circle, pink. 
bob.forward(125)
bob.color('pink')
bob.begin_fill()
bob.circle(50)
bob.end_fill()

#Fourth circle, orchid. 
bob.forward(125)
bob.color('orchid')
bob.begin_fill()
bob.circle(50)
bob.end_fill()

#Fifth circle, medium purple. 
bob.forward(125)
bob.color('mediumpurple')
bob.begin_fill()
bob.circle(50)
bob.end_fill()
