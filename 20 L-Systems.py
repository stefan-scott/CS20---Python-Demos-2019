#L-Systems:
import turtle
turtle.setup(1200,900)
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-500,0)
t.down()


def apply_rules(ch):
    #the rules are applied to a single character

    if ch == "L":
        return "+RF-LFL-FR+"
    elif ch == "R":
        return "-LF+RFR+FL-"
    else:
        return ch
    
def process_string(old_str):
    #loop through old_str and apply the L-system rules
    new_str = ""
    for c in old_str:
        new_str = new_str + apply_rules(c)
    return new_str

def create_l_system(num_iters, axiom):
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string

def draw_l_system(instructions, angle, distance):
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

commands = create_l_system(7, "L")
print(commands)
draw_l_system(commands, 90, 4)