import turtle, random  #turtle.py

#boilerplate code
window = turtle.Screen()
window.bgcolor("cadet blue")
roscoe = turtle.Turtle()

#get the turtle moving
roscoe.color("white")
roscoe.pensize(3)
roscoe.speed(0)

color_list = ["Coral", "BurlyWood", "DarkOrange", "Gold", "HoneyDew", "Tomato"]

#move in a loop
#for distance in range(0,300, 5): #[0,5,10,15,20 ...]
distance = 3
p_size = 1
while True:
    roscoe.color( random.choice(color_list) )
    roscoe.pensize(p_size)
    roscoe.fd(distance) #.fd()  == .forward()
    roscoe.rt(72)  #.rt() == .right()
    distance += 3
    p_size += 1
    if p_size > 20:
        p_size = 1
    


#put in the exit option
window.exitonclick()
