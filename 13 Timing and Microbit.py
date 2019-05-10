import time, microbit

while True:
    x_rotation = microbit.accelerometer.get_x()
##    if x_rotation > -200 and x_rotation < 200:
##        print("flat")
##    elif x_rotation <= -200:
##        print("tilted left")
##    else:
##        print("tilted right")
    y_rotation = microbit.accelerometer.get_y()
    if y_rotation > -200 and y_rotation < 200:
        print("flat")
    elif y_rotation <= -200:
        print("tilted forward")
    else:
        print("tilted backwards")
        








##for letter in ["A", "B", "C", "I"]:
##    microbit.display.show(letter)
##    time.sleep(0.5)
##
##for letter in "GO BEARS!!":
##    microbit.display.show(letter)
##    time.sleep(0.5)