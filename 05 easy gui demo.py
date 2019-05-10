import easygui_qt as easy
import random

#for i in range(30):
#    print(random.randint(0,100))

#for i in range(30):
#    print(random.uniform(0,100))

foods = ["perogies", "pizza", "plums", "pistachio", "peanuts"]
for i in range(10):
    print(random.choice(foods))
#start with some user input
#first_name = easy.get_string("What is your first name? ")
#last_name = easy.get_string("What is your last name? ")

#display the result
#easy.show_message("Hello there, " + first_name + " " + last_name)

#foods = ["perogies", "pizza", "plums", "pistachio", "peanuts"]
#choice = easy.get_choice("Pick a food: ", "P Foods", foods)
#print(choice)

#password = easy.get_password("What is the password: ", "PASSWORD")
#print(password)
