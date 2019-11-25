import microbit, time, turtle

window = turtle.Screen()
philip = turtle.Turtle()

while True:
    philip.fd(5) #always go forward a bit
    x_rotation = microbit.accelerometer.get_x()
    
    if x_rotation < - 300:
        philip.left(4)
    elif x_rotation > 300:
        philip.right(4)
    #ELSE (-300 <= x_rotation <= 300)
        
    # Neg value == left turn
    # Pos value == right turn
    print(x_rotation)
    time.sleep(0.1)



# for letter in ["S","A","S","K","A","T","C","H","E","W","A","N"]:
#     microbit.display.show(letter)
#     time.sleep(0.5)
# 
# for letter in "Roughriders":
#     microbit.display.show(letter)
#     time.sleep(0.5)
