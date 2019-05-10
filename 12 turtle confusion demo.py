import turtle, random

roscoe = turtle.Turtle()
reginald = turtle.Turtle()

wn = turtle.Screen()

def plus(side_length, a_turtle):
    """A function for having a turtle draw a plus sign.
side_length -> int
a_turtle -> turtle
"""
    for i in range(4):
        a_turtle.fd(side_length)
        a_turtle.right(90)
        a_turtle.fd(side_length)
        a_turtle.left(90)
        a_turtle.fd(side_length)
        a_turtle.left(90)
roscoe.speed(0)
roscoe.up()
roscoe.goto(-200,200)
roscoe.down()
#First Shape - multiple plus signs
for i in range(4):
    plus(20, roscoe)
    roscoe.left(90)




##reginald.up()
##reginald.goto(150,0)
##reginald.down()
##plus(100, reginald)
    
##turtle_list = []
##color_list = ["red","blue","yellow", "orange","black"]
##
##for i in range(6):
##    t = turtle.Turtle()
##    t.color(random.choice(color_list))
##    turtle_list.append(t)
##
##for steps in range(100):
##    for i in range(6):
##        current_turtle = turtle_list[i]
##        current_turtle.left(i)
##        current_turtle.fd(5)
    

