#First Program - Age in Days

#Ask for some input data
name = input("What is your name? ")
age = input("What is your age in years? ")

age = int(age) #convert age from a str to an int
age_in_days = age * 365.25

#Print out final message
print("Hello,", name , ". You are", age_in_days, "days old!")
