import microbit, time

def fade(b): #"4"
    return (b*5+":")*4+b*5

bright = 0
while True:
    microbit.display.show(microbit.Image(fade(str(bright))))
    bright += 1
    if bright > 9: bright = 0
    time.sleep(0.1)