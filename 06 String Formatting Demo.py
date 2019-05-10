#String Formatting Demo:

name = "Stefan"
grade = -1

#say something like "name is in grade ___. good job"
result_string = name + " is in grade " + str(grade) + ". Good job"
print(result_string)

result_string = f"""{name} is in grade {grade}.
Good job!"""
print(result_string)

result_string = f"NAME\t\tGRADE\n{name}\t\t{grade}"
print(result_string)