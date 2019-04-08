#Functions with Return Values

def larger_than_10(number):
    # Returns true if the input is larger than 10
    # False, if it is not.
    if number > 10: return True
    else: return False

user_number = int(input("Enter a number: "))
while larger_than_10(user_number):
    print("That's too high, go lower!")
    user_number = int(input("Enter a number: "))  