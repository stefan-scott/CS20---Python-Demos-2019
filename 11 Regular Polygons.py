import turtle

#Create a screen, and create a turtle
win = turtle.Screen()
roscoe = turtle.Turtle()

#Function for Triangle:
def triangle(side_length):
    for i in range(3):
        roscoe.forward(side_length)
        roscoe.left(120)
        
#function for Square
def square(side_length):
    for i in range(4):
        roscoe.fd(side_length)
        roscoe.left(90)
        
#function for Pentagon
def pentagon(side_length):
    for i in range(5):
        roscoe.fd(side_length)
        roscoe.left(72)
        
def r_poly(x,y,s):
    #Position the Turtle
    roscoe.up()
    roscoe.goto(x,y)
    roscoe.down()
    
    #Draw the Shape
    for i in range(s):
        roscoe.fd(300/s)
        roscoe.left(360/s)
#5,7,10,15,39
        
r_poly(-350,0,5)
r_poly(-175,0,7)
r_poly(0,0,39)
        
    


#Practice Moving the Turtle:
