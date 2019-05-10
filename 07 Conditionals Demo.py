def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    return not is_even(n)

















def letter_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


    