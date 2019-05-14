import microbit, time, random
#list to represent the 5x5 pixel grid
grid = [ [5,0,0,0,0],
         [0,5,0,0,0],
         [0,0,5,0,0],
         [0,0,0,5,0],
         [0,0,0,0,5] ]

def show_grid():
    result = ""
    for row in grid:
        for col in row:
            result = result + str(col)
        result += ":"
    result = result[0:-1]
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x, y, val):
    #x and y values from 0-4
    grid[y][x] = val
    show_grid()

object_x = 3
object_y = 0
set_pixel(object_x, object_y, 9)

while True:
    time.sleep(0.5)
    object_y += 1
    if (object_y > 4):
        object_y = 0
        object_x = random.randint(0,4)
    #erase previous object, draw new object
    set_pixel(object_x, object_y, 9)
    set_pixel(object_x, object_y-1, 0)

            
        
    


