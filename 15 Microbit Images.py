#micro:bit custom images
import microbit, time, random
THRESHOLD = -300

dice1 = "33333:" \
        "30003:" \
        "30903:" \
        "30003:" \
        "33333"

dice2 = "33333:" \
        "30003:" \
        "39093:" \
        "30003:" \
        "33333"

dice3 = "33333:" \
        "39003:" \
        "30903:" \
        "30093:" \
        "33333"

dice4 = "33333:" \
        "39093:" \
        "30003:" \
        "39093:" \
        "33333"

dice5 = "33333:" \
        "39093:" \
        "30903:" \
        "39093:" \
        "33333"

dice6 = "33333:" \
        "39093:" \
        "39093:" \
        "39093:" \
        "33333"

dice_images = [dice1, dice2, dice3, dice4, dice5, dice6]
microbit.display.show(microbit.Image(random.choice(dice_images)))

while True:
    motion = microbit.accelerometer.get_z()
    print(motion)
    if motion > THRESHOLD:
        microbit.display.show(microbit.Image(random.choice(dice_images)))
        time.sleep(0.1)
    time.sleep(0.1)
