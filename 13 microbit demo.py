#Turtle Racing Game
import microbit, time, turtle, random
FINISH_X = 300

#set up the turtles and window
wn = turtle.Screen()
player1 = turtle.Turtle()
player2 = turtle.Turtle()
referee = turtle.Turtle()

#initialize the turtles
player1.up()
player2.up()
player1.goto(-300,100)
player2.goto(-300,-100)

#make the finish line
referee.up()
referee.goto(FINISH_X,400)
referee.down()
referee.goto(FINISH_X,-400)

while True:
    if microbit.button_a.was_pressed():
        player1.fd(20)
    #computer player
    player2.fd(random.randint(1,3))
    
    #determine winner?
    if player1.xcor() > FINISH_X:
        #print("Player 1 Wins!!!")
        referee.up()
        referee.goto(0,0)
        referee.down()
        referee.write("Player One Wins!!", True, align="center", font=("Arial", 30, "normal"))
        break
            # referee.write("Player One Wins!!", True,
            # align="center", font=("Arial", 30, "normal"))
    if player2.xcor() > FINISH_X:
        #print("Player 2 Wins!!!")
        break
    



