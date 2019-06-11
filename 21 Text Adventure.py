#Choose Your Own Aventure Demo
import random
#CHAPTER ONE  - Wake Up!
print("Welcome to this game. You're a high school student")
clothing = input("You wake up - what will you wear? (dressy) (preppy) (super casual)")

#CHAPTER TWO - Get to School!
print("Each day you either walk to school, or take the bus")
transport = input("Which do you do today? (walk) (bus)")

if transport.lower() == "walk":
    #user chooses to walk to school
    print("""The walk was uneventful. When you arrive,
          you remember you have a field trip""")
    item = input("""What do you grab from your locker?
            (5 dollar bill) (Comb) (Stick of Gum)""")
    print("""Your field trip is to the law offices. You
        are easily distracted and get separated from the
        group""")
else:
    #riding the bus to school
    print("""You snooze on the bus and miss your stop!
          The bus breaks down at the law offices and you
          get off""")
    choice = input("""On your way off, you notice a stick
                  of gum on the ground. Do you pick it up
                  (yes) (no)""")
    if choice.upper() == "YES":
        item = "Stick of Gum"

#CHAPTER THREE - Which way to go?
print("""You find yourself in a hallway you don't
recognize. You could go left or right""")
direction = input("Which way do you go (left) (right)")
if direction.lower() == "right":
    #ENDGAME branch 1
    print("You find your school group, and rejoin them!")
else:
    #Choosing to go left
    print("""You see a door open just a crack, with
            light inside""")
    enter = input("Do you go in? (yes) (no)")
    if enter.lower() == "no":
        #ENDGAME Branch 2
        print("""You turn around and see your friends.
              You rejoin the field trip and enjoy the day""")
    else:
        #ENDGAME 3 - Trying to get a sweet job
        print("""You find yourself about to go into a
              job interview - you have 1 minute to prepare
              """)
        use_item = input("Do you want to use your item")
        chance = 45
        if item.upper() == "STICK OF GUM": #+10% fresh breath
            chance = chance + 10
        elif item.upper() == "COMB": # +20% nice hair
            chance = chance + 20
        elif item.upper() == "5 DOLLAR BILL": # -100% Bribe
            chance = chance - 100
        
        #Modify chance based on our clothing selection
        if clothing.lower() == "dressy" or clothing.lower() == "preppy":
            chance += 25
        elif clothing.lower() == "super casual":
            chance -= 30
        
        #Find the result!
        random_num = random.randint(0,99)
        if chance < 0: #guaranteed failure
            print("""You go into the interview and totally embarass
                  yourself. They say try again in 10 years...""")
        else:
            if random_num <= chance: #success
                print("""You fake it until you make it and get the
                      job! When will you find time for math homework?""")
            else:
                print("""Your Interview went well, but it didn't
                      quite pan out. Better luck next time!""")
            
    
    
    



