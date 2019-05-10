#Micro:bit Images
import microbit, random, time

images = []

#make a loop with the counting variable being 1-12
##for num in range(1,13):
##    images.append(microbit.Image.CLOCK+str(num))
images.append(microbit.Image.CLOCK1)
images.append(microbit.Image.CLOCK2)
images.append(microbit.Image.CLOCK3)
images.append(microbit.Image.CLOCK4)
images.append(microbit.Image.CLOCK5)
images.append(microbit.Image.CLOCK6)
images.append(microbit.Image.CLOCK7)
images.append(microbit.Image.CLOCK8)
images.append(microbit.Image.CLOCK9)
images.append(microbit.Image.CLOCK10)
images.append(microbit.Image.CLOCK11)
images.append(microbit.Image.CLOCK12)

current = 0
while True:
    microbit.display.show(images[current])
    current += 1  #current = current + 1
    if current == 12:
        current = 0
    time.sleep(0.01)
    