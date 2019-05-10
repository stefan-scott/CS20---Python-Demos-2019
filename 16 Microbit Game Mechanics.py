##dice6 = "33333:" \
##        "39093:" \
##        "39093:" \
##        "39093:" \
##        "33333"
import microbit
player_x = 3

def create_screen(player_x): #0-4
    line1 = "00000:"
    line2 = "00000:"
    line3 = "00000:"
    line4 = "00000:"
    line5 = ["0","0","0","0","0"]
    line5[player_x]="9"
    line5 = line5[0]+line5[1]+line5[2]+line5[3]+line5[4]
    return line1 + line2 + line3 + line4 + line5
    
current_image = create_screen(player_x)
microbit.display.show(microbit.Image(current_image))

while True:
    if microbit.button_a.was_pressed():
        #moving to left
        if player_x > 0:
            player_x = player_x - 1
        else:
            player_x = 4
    
    if microbit.button_b.was_pressed():
        #moving to right
        if player_x < 4:
            player_x = player_x + 1
        else:
            player_x = 0
        
    #Update the Screen of the Micro:bit
    current_image = create_screen(player_x)
    microbit.display.show(microbit.Image(current_image))
    
    