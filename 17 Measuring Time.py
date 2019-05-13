import microbit, time
#Basic Timer Example
start_time = time.time()
elapsed_time = 0
while elapsed_time < 5:
    end_time = time.time()
    elapsed_time = end_time - start_time
    if microbit.button_a.was_pressed():
        print("You waited",elapsed_time,"seconds")
        start_time = end_time
print("You waited too long!")