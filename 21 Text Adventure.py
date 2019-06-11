#Choose Your Own Aventure Demo

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

#CHAPTER THREE
    
    
    
    



